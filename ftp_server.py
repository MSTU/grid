from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from multigrid.conf import config

authorizer = DummyAuthorizer()
authorizer.add_user(config.FTP_LOGIN, config.FTP_PASSWORD, config.FTP_PATH, perm="elradfmw")
#authorizer.add_anonymous("/home/nobody")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((config.IP_ADDRESS, config.FTP_PORT), handler)
server.serve_forever()
