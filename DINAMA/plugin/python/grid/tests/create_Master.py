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
import Master
import multiprocessing as mp
import PyroMaster
from conf import ConfigMaster
import Constants


def main():
	master = PyroMaster.PyroMaster()
	daemon=Pyro4.Daemon(host = ConfigMaster.MASTER_IP_ADDRESS, port = ConfigMaster.PORT)
	daemon.register(master, Constants.MASTER_NAME)
	master.RunBalancer()
	daemon.requestLoop()

if __name__=="__main__":
	p = mp.Process(target=main)
	p.daemon = True
	p.start()
	file = open('master_pid.txt','w')
	file.write(str(p.pid))
	file.close()
	p.join()