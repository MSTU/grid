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

import re # ��� ������������� ���������� ���������
import subprocess # ��� ������ �������� ��������� �����
import os # ��� ��������� �� ���������
import sys # ��� ����������� ���� ������������ �������
import hashlib # ��� ������ ���� �����
import Constants
import Launcher


class ModelicaSolver(Launcher.Launcher):
    # ������������� �������
    # object initialization
    def __init__(self):
        self.name = "ModelicaDynamic"
        self.MOS_filename = 'script.mos' # Host will use this name to create its own MOS file

    # �������� ������ � �������
    # preparing of data for calculation
    # writes dictionary in Loadcase variable inData
    # keys are mos and mo filenames; values are lists of the file strings
    def LoadData(self, lc):
        files_dict = dict() #files dictionary, where keys are filenames and values are list of file strings
        with open(lc.Scheme, 'r') as f:
            mos = f.readlines()
        files_dict[self.MOS_filename] = mos
        files_dict.update(self.CreateMOfilesDict(lc.Scheme))
        lc.inData = files_dict

    # �������� ������ *.mo � *.mos � ����� � ������ ���������� ������ Loadcase.Name.
    # ��������� exe-����� � �� �������
    def Compile(self, MOS_filename):
        if sys.platform.startswith('win'):
            command = '%OPENMODELICAHOME%/bin/omc.exe ' + MOS_filename
            print 'compiling...'
            subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
            print 'compiled'
        elif sys.platform.startswith('linux'):
            print 'compiling...'
            subprocess.call(["omc", MOS_filename])
            print 'compiled'
        else:
            print 'can not determine your platform'
            return Constants.TASK_ERROR

    # ������ ������� ����� � ������������� �� �����������
    # scheme - ���� � ����� ������ (mos, mo, py, sch)
    # ������� ���������� � �� ��������
    def Run(self, loadcase, parameters):
        cwd = os.getcwd()
        #if not os.path.exists(id): os.makedirs(id)
        #os.chdir(id)
        if not os.path.exists(loadcase.Name): os.makedirs(loadcase.Name)
        os.chdir(loadcase.Name)

        # Host creates all required files
        for k, v in loadcase.inData.iteritems():
            self.CreateFileFromList(v, k)

        class_name = self.GetClassName(self.MOS_filename)
        ''' something for checking file's checksum
        if sys.platform.startswith('win'):
            # ��������, ���������� �� ��� exe-���� ������ ��� ���
            if (os.path.isfile(class_name + '.exe')):
                pass
            else:
                self.Compile(self.MOS_filename) # ��������� exe-����� �� mos-�����
                hash = self.hashFile(class_name + '.exe', hashlib.sha256())
                with open(class_name + '.txt', 'w') as h:
                    h.write(hash)
        elif sys.platform.startswith('linux'):
            if (os.path.isfile(class_name)):
                pass
            else:
                self.Compile(self.MOS_filename) # ��������� exe-����� �� mos-�����
                hash = self.hashFile(class_name + '.exe', hashlib.sha256())
                with open(class_name + '.txt', 'w') as h:
                    h.write(hash)
        else:
            print 'can not determine your platform'
            return Constants.TASK_ERROR
        '''

        PAR_filename = 'pl.txt'
        RES_filename = 'results.plt'

        # �������� ������ ������� ���������� �� �������� ������� ����������
        self.CreateParFilesFromParDicts(PAR_filename, parameters.GetParameters())

        if sys.platform.startswith('win'):
            if (os.path.isfile(class_name + '.exe')):
                pass
            else:
                self.Compile(self.MOS_filename) # ��������� exe-����� �� mos-�����
            command = class_name + '.exe -overrideFile ' + PAR_filename + ' -r ' + RES_filename
            print 'executing'
            subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
            print 'executed'

        elif sys.platform.startswith('linux'):
            if (os.path.isfile(class_name)):
                pass
            else:
                self.Compile(self.MOS_filename) # ��������� exe-����� �� mos-�����
            command = ['-overrideFile'] + [PAR_filename] + ['-r'] + [RES_filename]
            print 'executing'
            subprocess.call(["./" + class_name] + command)
            print 'executed'

        else:
            print 'can not determine your platform'
            return Constants.TASK_ERROR

        # ��������� ������� �������� ����������
        self.CreateResultsDict(RES_filename, parameters)
        print parameters.GetResults()

        os.chdir(cwd)
        return Constants.TASK_SUCCESS
    # using this function you can specify simulate parameters listed in MOS file
    # for instance: setSimulateParameters('mos_file.mos', 'stopTime', 35.5)
    def setSimulateParameter(self, MOS_filename, par_name, par_value):
        temp_file = open('temp', 'w')
        with open(MOS_filename, 'r') as f:
            for line in f:
                if(not line.startswith('simulate')):
                    temp_file.write(line)
                else:
                    temp_file.write(re.sub(par_name + '( )?=( )?(\d)+(\.(\d)+)*', par_name + ' = ' + par_value, line))
                    #par_name + '( )?=( )?(\d)+(\.(\d)+)*
                    #line matches above pattern if it contains something like:
                    #par_name(1 or 0 spaces)=(1 or 0 spaces)(any number of digits)
                    #par_name(1 or 0 spaces)=(1 or 0 spaces)(any number of digits).(1 digit or more)
        temp_file.close()
        #now temp file is a full copy of MOS file with one difference in parameter value
        #parameter named "par_name" has changed its old value to "par_value"
        os.unlink(MOS_filename) #deleting old MOS file
        os.rename(temp_file.name, MOS_filename)
        #changed temp filename to MOS filename, so we can use old filename with new content

    # ���������� ��� ������, ����������� �� mos-����� (simulate(className, ...))
    # ���������� ��� ��������� ���� ������ �� ����� C, ��� ���������� � �������
    def GetClassName(self, MOS_filename):
        className = None
        with open(MOS_filename, 'r') as f:
            for line in f:
                if (not line.startswith('simulate')):
                    pass
                else:
                    className = re.split('[(,]', line)[1]

        return className

    # Returns file's checksum
    # filename - name of file; hasher - hash algorithm (md5, sha1, sha256, ...);
    # blocksize - the internal block size of the hash algorithm in bytes
    def hashFile(self, filename, hasher, blocksize = 8192):
        with open(filename, 'rb') as f:
            buf = f.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(blocksize)

        return hasher.hexdigest()

    # Returns a dictionary, where keys are mo filenames and values are list of mo file strings
    # dictionary is created using mos file located at MOS_file_path
    def CreateMOfilesDict(self, MOS_file_path):
        files_dict = dict()
        cwd = os.getcwd()
        #filenames.append(re.search('(\w)+\.mos', MOS_file_path).group())
        with open(MOS_file_path, 'r') as mos:#mos = open(MOS_file_path, 'r')
            if(MOS_file_path.rpartition('/')[0] != 0):
                os.chdir(MOS_file_path.rpartition('/')[0])
            for line in mos:
                if (not line.startswith('loadFile')):
                    pass
                else:
                    mo_filename = re.search('(\w)+\.mo', line).group()
                    #mo_filepath = MOS_file_path.rpartition('/')[0] + '/' + mo_filename
                    with open(re.split('"', line)[1], 'r') as mo:
                        mo_file = mo.readlines()
                        files_dict[mo_filename] = mo_file
                        #filenames.append(re.search('(\w)+\.mo', line).group())
        os.chdir(cwd)

        return files_dict

    # ������� ���� � ��������� filename �� ������ ����� stringList
    # ������ ���������� ���������� stringList: ['loadModel(Modelica);\n', 'getErrorString();\n', ...]
    def CreateFileFromList(self, stringList, filename):
        # �������� �����
        with open(filename, 'w') as f:
            for line in stringList:
                f.write(line)

    # ��������� ������ ������� ���������� �� �������� ������� ���������� ma1, ma2, ...
    def CreateParFilesFromParDicts(self, par_filename, par_dic):
        with open(par_filename, 'w') as PAR_file:
            for k, v in par_dic.iteritems():
                PAR_file.write(k + '=' + str(v) + '\n')

    # �������� ������� ����������� �� ����� ����������� RES_filename
    # ��� ������� ���������� parameters
    # RES_filename - ��� ����� �����������
    def CreateResultsDict(self, RES_filename, MA_object):
        curvesNumber = 0 #���������� �������� ����������
        result_dict = dict() #������� �����������
        value_list = list() #������ �������� ��� �������� ��������� ���������
        print os.getcwd()

        with open(RES_filename, 'r') as f:
            for line in f:
                if (not line.startswith('DataSet: ')):
                    continue
                curvesNumber += 1
                MA_object.SetCurves(curvesNumber)
                key = re.split('DataSet: ', line)[1][:-1]
                for line in f:
                    if (line != '\n'):
                        value_list.append(float(re.split('[\d.e-], ', line)[1][:-1]))
                    else:
                        break
                tmp = list(value_list[:-1]) #������ ��������� �������,
                #�.�. value_list[���������] = value_list[���������-1]
                result_dict[key] = tmp
                del value_list[:] #�������� ���������� ����� ������

        MA_object.SetLayer(len(tmp))
        MA_object.SetResults(result_dict)
        MA_object.SetStatus(Constants.TASK_SUCCESS)

    def GetLog(self):
        pass
