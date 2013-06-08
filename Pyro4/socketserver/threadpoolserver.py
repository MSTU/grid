"""
Socket server based on a worker thread pool. Doesn't use select.

Uses a single worker thread per client connection.

Pyro - Python Remote Objects.  Copyright by Irmen de Jong (irmen@razorvine.net).
"""

from __future__ import with_statement
import socket, logging, sys, os
import struct
from Pyro4 import socketutil, errors
import Pyro4.tpjobqueue

log=logging.getLogger("Pyro4.socketserver.threadpool")


class ClientConnectionJob(object):
    """
    Takes care of a single client connection and all requests
    that may arrive during its life span.
    """
    def __init__(self, clientSocket, clientAddr, daemon):
        self.csock = socketutil.SocketConnection(clientSocket)
        self.caddr = clientAddr
        self.daemon = daemon

    def __call__(self):
        if self.handleConnection():
            while True:
                try:
                    self.daemon.handleRequest(self.csock)
                except (socket.error, errors.ConnectionClosedError):
                    # client went away.
                    log.debug("disconnected %s", self.caddr)
                    break
                except errors.SecurityError:
                    log.debug("security error on client %s", self.caddr)
                    break
            self.csock.close()

    def handleConnection(self):
        # connection handshake
        try:
            if self.daemon._handshake(self.csock):
                return True
        except (socket.error, errors.PyroError):
            x=sys.exc_info()[1]
            log.warn("error during connect: %s", x)
            self.csock.close()
        return False

    def interrupt(self):
        """attempt to interrupt the worker's request loop"""
        try:
            self.csock.sock.shutdown(socket.SHUT_RDWR)
            self.csock.sock.setblocking(False)
        except socket.error:
            pass
        if hasattr(socket, "SO_RCVTIMEO"):
            # setting a recv timeout seems to break the blocking call to recv() on some systems
            try:
                self.csock.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, struct.pack("ii", 1,1))
            except socket.error:
                pass
        self.csock.close()



class SocketServer_Threadpool(object):
    """transport server for socket connections, worker thread pool version."""
    def init(self, daemon, host, port, unixsocket=None):
        log.info("starting thread pool socketserver")
        self.daemon = daemon
        self.sock=None
        bind_location=unixsocket if unixsocket else (host,port)
        self.sock=socketutil.createSocket(bind=bind_location, reuseaddr=Pyro4.config.SOCK_REUSE, timeout=Pyro4.config.COMMTIMEOUT, noinherit=True)
        self._socketaddr=self.sock.getsockname()
        if self._socketaddr[0].startswith("127."):
            if host is None or host.lower()!="localhost" and not host.startswith("127."):
                log.warn("weird DNS setup: %s resolves to localhost (127.x.x.x)", host)
        if unixsocket:
            self.locationStr="./u:"+unixsocket
        else:
            host=host or self._socketaddr[0]
            port=port or self._socketaddr[1]
            if ":" in host:  # ipv6
                self.locationStr="[%s]:%d" % (host, port)
            else:
                self.locationStr="%s:%d" % (host, port)
        self.jobqueue = Pyro4.tpjobqueue.ThreadPooledJobQueue()
        log.info("%d workers started", self.jobqueue.workercount)

    def __del__(self):
        if self.sock is not None:
            self.sock.close()
        if self.jobqueue is not None:
            self.jobqueue.close()

    def __repr__(self):
        return "<%s on %s, %d workers, %d jobs>" % (self.__class__.__name__, self.locationStr,
            self.jobqueue.workercount, self.jobqueue.jobcount)

    def loop(self, loopCondition=lambda: True):
        log.debug("threadpool server requestloop")
        while (self.sock is not None) and loopCondition():
            try:
                self.events([self.sock])
            except socket.error:
                x=sys.exc_info()[1]
                err=getattr(x, "errno", x.args[0])
                if not loopCondition():
                    # swallow the socket error if loop terminates anyway
                    # this can occur if we are asked to shutdown, socket can be invalid then
                    break
                if err in socketutil.ERRNO_RETRIES:
                    continue
                else:
                    raise
            except KeyboardInterrupt:
                log.debug("stopping on break signal")
                break
        log.debug("threadpool server exits requestloop")

    def events(self, eventsockets):
        """used for external event loops: handle events that occur on one of the sockets of this server"""
        # we only react on events on our own server socket.
        # all other (client) sockets are owned by their individual threads.
        assert self.sock in eventsockets
        try:
            csock, caddr=self.sock.accept()
            log.debug("connected %s", caddr)
            if Pyro4.config.COMMTIMEOUT:
                csock.settimeout(Pyro4.config.COMMTIMEOUT)
            self.jobqueue.process(ClientConnectionJob(csock, caddr, self.daemon))
        except socket.timeout:
            pass  # just continue the loop on a timeout on accept

    def close(self, joinWorkers=True):
        log.debug("closing threadpool server")
        if self.sock:
            sockname=None
            try:
                sockname=self.sock.getsockname()
            except socket.error:
                pass
            try:
                self.sock.close()
                if type(sockname) is str:
                    # it was a Unix domain socket, remove it from the filesystem
                    if os.path.exists(sockname):
                        os.remove(sockname)
            except Exception:
                pass
            self.sock=None
        self.jobqueue.close()
        for worker in self.jobqueue.busy.copy():
            if worker.job is not None:
                worker.job.interrupt()   # try to break all busy workers
        if joinWorkers:
            self.jobqueue.drain()

    @property
    def sockets(self):
        # the server socket is all we care about, all client sockets are running in their own threads
        return [self.sock]

    def wakeup(self):
        interruptSocket(self._socketaddr)


def interruptSocket(address):
    """bit of a hack to trigger a blocking server to get out of the loop, useful at clean shutdowns"""
    try:
        sock=socketutil.createSocket(connect=address, keepalive=False, timeout=None)
        if sys.version_info<(3, 0):
            sock.send("!"*16)
        else:
            sock.send(bytes([1]*16))
        sock.close()
    except socket.error:
        pass

