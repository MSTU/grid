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

import subprocess
import os
import re
import sys
import Constants
import Launcher


class LSDYNASolver(Launcher.Launcher):
    # object initialization
    def __init__(self):
        Launcher.Launcher.__init__(self)
        self.name = "ANSYS_LS-DYNA"
        self.exec_options = ["G", "D", "F", "T", "A", "M", "S", "Z",
                "L", "B", "W", "E", "X", "C", "K", "V",
                "Y", "BEM", "MEMORY", "NCPU",
                "PARA", "ENDTIME", "NCYCLE",
                "JOBID", "D3PROP", "GMINP", "GMOUT",
                "MCHECK"]
        #self.exec_pars_dict = dict.fromkeys(keys)

    # Loads content of *.k file in special variable inData
    def LoadData(self, lc):
        if not os.path.isfile(lc.Scheme):
            print "ERROR"
            print lc.Scheme + " does not exist"
            return None
        with open(lc.Scheme, 'r') as f:
            lc.inData = f.readlines()

    def Run(self, loadcase, ma_object):
        if loadcase.inData is None:
            print "ERROR"
            print "inData contains nothing"
            return Constants.TASK_ERROR
        cwd = os.getcwd()
        if not os.path.exists(loadcase.Name): os.makedirs(loadcase.Name)
        os.chdir(loadcase.Name)
        log_filename = "LS-DYNA_log"
        try:
            log_file = open(log_filename, "w")
        except IOError:
            print "Can not create \"" + log_filename + "\""
            return Constants.TASK_ERROR
        # loadcase.Scheme.rpartition("/")[2] - actual filename
        #for example
        #path = /home/user/ls-dyna/file.k
        #path.rparition("/")[2] = "file.k"
        k_filename = loadcase.Scheme.rpartition("/")[2]
        self.CreateFileFromList(loadcase.inData, k_filename)
        #lsdyna is a list that contains the only string to launch ANSYS LS-DYNA
        #example for ANSYS version 14.5: ["/path_to_lsdyna145/lsdyna145"]
        lsdyna = self.CreateLSDYNACommand()
        #options is a list of option strings: ["... = ...", "... = ..."]
        # there are options for LS DYNA command in ModelAnalysis parameters' dictionary
        user_dict = {}
        user_dict.update(ma_object.GetParameters())
        if(user_dict):
            options = self.CreateOptionsCommand(user_dict)
            print options
        else:
            options = []
        options += ["I=" + k_filename]
        if(len(loadcase.ResultFile) != 0):
            options += ["O=" + loadcase.ResultFile]

        if sys.platform.startswith('win'):
            pass
        elif sys.platform.startswith('linux'):
            print 'executing LS-DYNA'
            print lsdyna + options
            subprocess.call(lsdyna + options, stdout = log_file)
            print 'LS-DYNA finished'
        else:
            print 'Сan not determine your platform'
            return Constants.TASK_ERROR
        log_file.close()
        return_code = self.CheckTermination(log_filename)
        os.chdir(cwd)

        if(return_code == 1):
            return Constants.TASK_SUCCESS
        else:
            print "ERROR Termination"
            print "Check \"" + log_filename + "\" for a more detailed description"
            return Constants.TASK_ERROR

    # Creates file from list of strings
    def CreateFileFromList(self, stringList, filename):
        with open(filename, 'w') as f:
            for line in stringList:
                f.write(line)

    # Creates string to launch ANSYS LS-DYNA
    def CreateLSDYNACommand(self):
        ANSYS_version = self.GetANSYSVersion()
        if ANSYS_version is not None:
            lsdyna_command = ["/ansys_inc/v" + ANSYS_version + "/ansys/bin/lsdyna" + ANSYS_version]
            return lsdyna_command
        else:
            return []

    # Creates string of options for LS-DYNA
    def CreateOptionsCommand(self, user_dict):
        # fill exec_dict
        exec_dict = {}
        options_command = []
        for key, value in user_dict.iteritems():
            if key.upper() in self.exec_options:
                exec_dict[key] = value
            else:
                print "invalid option on the command line " + key
                print "skipping it"
        for key, value in exec_dict.iteritems():
            options_command += [key + "=" + str(value)]

        return options_command

    # Determines ANSYS version
    def GetANSYSVersion(self):
        if sys.platform.startswith('win'):
            pass
        elif sys.platform.startswith('linux'):
            if(os.path.isdir("/ansys_inc")):
                dir_list = os.listdir("/ansys_inc")
                for line in dir_list:
                    temp = re.search("v[\d]+", line)
                    if temp is not None:
                        version = temp.group(0)[1:]
                        return version
            else:
                print "Сan not locate your ANSYS installation directory"
        else:
            print 'Сan not determine your platform'
        return None

    def CheckTermination(self, log_filename):
        normal_string = "Normaltermination"
        flag = -1
        try:
            log_file = open(log_filename, "r")
        except IOError:
            print "Can not open \"" + log_filename + "\" for reading"
            return None
        #string about termination is the last line
        #we move 85 bytes from the end to the beginning of the file,
        #because last line is approximately < 90 bytes in length

        #we are using line.replace(" ", "") to delete all whitespaces,
        #because there are too many of them
        log_file.seek(-90, 2)
        for line in log_file:
            if normal_string in line.replace(" ", ""):
                flag = 1

        log_file.close()
        return flag
