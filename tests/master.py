# -*- coding: cp1251 -*-

#***************************************************************************
#
#    copyright            : (C) 2013 by Valery Ovchinnikov (LADUGA Ltd.)
#                                       Anton Lapshin
#                                       Anton Kargin
#    email                : laduga@laduga.com
#***************************************************************************
#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License as published by  *
#*   the Free Software Foundation; either version 2 of the License, or     *
#*   (at your option) any later version.                                   *
#*                                                                         *
#***************************************************************************/

import Pyro4
import sys
import Master
import multiprocessing as mp
from conf import ConfigMaster
import Constants
from daemon import Daemon


class MasterDaemon(Daemon):

	def run(self):
		self.daemon.requestLoop()
		self.master = Master.Master()
		self.daemon = Pyro4.Daemon(host = ConfigMaster.MASTER_IP_ADDRESS, port = ConfigMaster.PORT)
		self.daemon.register(self.master, Constants.MASTER_NAME)
		self.master.RunBalancer()

if __name__ == "__main__":
	daemon = MasterDaemon('/tmp/master_daemon.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)