"""
Socket server based on socket multiplexing. Doesn't use threads.

Pyro - Python Remote Objects.  Copyright by Irmen de Jong (irmen@razorvine.net).
"""

import socket, select, sys, logging, os
from Pyro4 import socketutil, errors
import Pyro4

log=logging.getLogger("Pyro4.socketserver.multiplexed")


class MultiplexedSocketServerBase(object):
    """base class for multiplexed transport server for socket connections"""
    def init(self, daemon, host, port, unixsocket=None):
        log.info("starting multiplexed socketserver")
        self.sock=None
        bind_location=unixsocket if unixsocket else (host, port)
        self.sock=socketutil.createSocket(bind=bind_location, reuseaddr=Pyro4.config.SOCK_REUSE, timeout=Pyro4.config.COMMTIMEOUT, noinherit=True)
        self.clients=[]
        self.daemon=daemon
        sockaddr=self.sock.getsockname()
        if sockaddr[0].startswith("127."):
            if host is None or host.lower()!="localhost" and not host.startswith("127."):
                log.warn("weird DNS setup: %s resolves to localhost (127.x.x.x)", host)
        if unixsocket:
            self.locationStr="./u:"+unixsocket
        else:
            host=host or sockaddr[0]
            port=port or sockaddr[1]
            if ":" in host:   # ipv6
                self.locationStr="[%s]:%d" % (host, port)
            else:
                self.locationStr="%s:%d" % (host, port)

    def __repr__(self):
        return "<%s on %s, %d connections>" % (self.__class__.__name__, self.locationStr, len(self.clients))

    def __del__(self):
        if self.sock is not None:
            self.sock.close()
            self.sock=None

    def events(self, eventsockets):
        """used for external event loops: handle events that occur on one of the sockets of this server"""
        for s in eventsockets:
            if s is self.sock:
                # server socket, means new connection
                conn=self._handleConnection(self.sock)
                if conn:
                    self.clients.append(conn)
            else:
                # must be client socket, means remote call
                try:
                    self.daemon.handleRequest(s)
                except (socket.error, errors.ConnectionClosedError, errors.SecurityError):
                    # client went away or caused a security error
                    s.close()
                    if s in self.clients:
                        self.clients.remove(s)

    def _handleConnection(self, sock):
        try:
            if sock is None:
                return
            csock, caddr = sock.accept()
            if Pyro4.config.COMMTIMEOUT:
                csock.settimeout(Pyro4.config.COMMTIMEOUT)
        except socket.error:
            x=sys.exc_info()[1]
            err=getattr(x, "errno", x.args[0])
            if err in socketutil.ERRNO_RETRIES:
                # just ignore this error for now and continue
                log.warn("accept() failed errno=%d, shouldn't happen", err)
                return None
            if err in socketutil.ERRNO_BADF or err in socketutil.ERRNO_ENOTSOCK:
                # our server socket got destroyed
                raise errors.ConnectionClosedError("server socket closed")
            raise
        try:
            conn=socketutil.SocketConnection(csock)
            if self.daemon._handshake(conn):
                return conn
        except (socket.error, errors.PyroError):
            x=sys.exc_info()[1]
            log.warn("error during connect: %s", x)
            csock.close()
        return None

    def close(self):
        log.debug("closing socketserver")
        if self.sock:
            sockname=None
            try:
                sockname=self.sock.getsockname()
            except socket.error:
                pass
            self.sock.close()
            if type(sockname) is str:
                # it was a Unix domain socket, remove it from the filesystem
                if os.path.exists(sockname):
                    os.remove(sockname)
        self.sock=None
        for c in self.clients:
            try:
                c.close()
            except Exception:
                pass
        self.clients=[]

    @property
    def sockets(self):
        socks=[self.sock]
        socks.extend(self.clients)
        return socks

    def wakeup(self):
        """bit of a hack to trigger a blocking server to get out of the loop, useful at clean shutdowns"""
        try:
            if sys.version_info<(3, 0):
                self.sock.send("!"*16)
            else:
                self.sock.send(bytes([1]*16))
        except socket.error:
            pass


class SocketServer_Poll(MultiplexedSocketServerBase):
    """transport server for socket connections, poll loop multiplex version."""

    def loop(self, loopCondition=lambda: True):
        log.debug("enter poll-based requestloop")
        poll=select.poll()
        try:
            fileno2connection={}  # map fd to original connection object
            poll.register(self.sock.fileno(), select.POLLIN | select.POLLPRI)
            fileno2connection[self.sock.fileno()]=self.sock
            while loopCondition():
                polls=poll.poll(1000*Pyro4.config.POLLTIMEOUT)
                for (fd, mask) in polls:
                    conn=fileno2connection[fd]
                    if conn is self.sock:
                        try:
                            conn=self._handleConnection(self.sock)
                        except errors.ConnectionClosedError:
                            log.info("server socket was closed, stopping requestloop")
                            return
                        if conn:
                            poll.register(conn.fileno(), select.POLLIN | select.POLLPRI)
                            fileno2connection[conn.fileno()]=conn
                    else:
                        try:
                            self.daemon.handleRequest(conn)
                        except (socket.error, errors.ConnectionClosedError, errors.SecurityError):
                            # client went away or caused a security error
                            try:
                                fn=conn.fileno()
                            except socket.error:
                                pass
                            else:
                                if fn in fileno2connection:
                                    poll.unregister(fn)
                                    del fileno2connection[fn]
                                conn.close()
        except KeyboardInterrupt:
            log.debug("stopping on break signal")
            pass
        finally:
            if hasattr(poll, "close"):
                poll.close()
        log.debug("exit poll-based requestloop")


class SocketServer_Select(MultiplexedSocketServerBase):
    """transport server for socket connections, select loop version."""

    def loop(self, loopCondition=lambda: True):
        log.debug("entering select-based requestloop")
        while loopCondition():
            try:
                rlist=self.clients[:]
                rlist.append(self.sock)
                try:
                    rlist, _, _=select.select(rlist, [], [], Pyro4.config.POLLTIMEOUT)
                except select.error:
                    if loopCondition():
                        raise
                    else:
                        # swallow the select error if the loopcondition is no longer true, and exit loop
                        # this can occur if we are shutting down and the socket is no longer valid
                        break
                if self.sock in rlist:
                    try:
                        rlist.remove(self.sock)
                    except ValueError:
                        pass  # this can occur when closing down, even when we just tested for presence in the list
                    try:
                        conn=self._handleConnection(self.sock)
                        if conn:
                            self.clients.append(conn)
                    except errors.ConnectionClosedError:
                        log.info("server socket was closed, stopping requestloop")
                        return
                for conn in rlist[:]:
                    if conn in self.clients:
                        rlist.remove(conn)
                        try:
                            self.daemon.handleRequest(conn)
                        except (socket.error, errors.ConnectionClosedError, errors.SecurityError):
                            # client went away or caused a security error
                            conn.close()
                            if conn in self.clients:
                                self.clients.remove(conn)
            except socket.timeout:
                pass   # just continue the loop on a timeout
            except KeyboardInterrupt:
                log.debug("stopping on break signal")
                break
        log.debug("exit select-based requestloop")
