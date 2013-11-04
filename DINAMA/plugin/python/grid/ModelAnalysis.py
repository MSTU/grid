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

# ����� ���������� � ����������� ������

class ModelAnalysis:
    # ������������� �������
    def __init__(self):
        self.par_dict = dict()                # ������� ����������
        self.result_dict = dict()            # ������� ������� ����������
        self.status = 1
        self.layer = 0                        # ���������� ��������� �����
        self.curvesNumber = 0                # ���������� �������� ����������


    def SetParameters(self, par_dict):
        self.par_dict = par_dict

    def GetParameters(self):
        return self.par_dict

    def GetParameter(self, name):
        return self.par_dict[name]

    def GetParameterValueList(self, name):
        return self.par_dict[name]

    def GetParameterValueFromLayer(self, name, layer):
        j = 0
        for i in self.par_dict[name]:
            if(j == layer-1):
                return i
            else:
                j += 1
        return None #if self.par_dict[name] has no such layer

    def AddResults(self, res_dict):
        self.result_dict.update(res_dict)

    def SetResults(self, res_dict):
        self.result_dict = res_dict

    def GetResults(self):
        return self.result_dict

    def GetStatus(self):
        return self.status

    def SetStatus(self, status):
        self.status = status

    # ���������� ��������� ����
    # layer - ����� ���� �� �������
    def SetLayer(self, Layer):
        if (Layer < 0):
            self.layer = 0
        else:
            self.layer = Layer

    # �������� ����� ��������� �����
    def GetLayerCount(self):
        return self.layer;

    # ���������� ����� �������� ����������
    def SetCurves(self, number):
        if (number < 0):
            self.curvesNumber = 0
        else:
            self.curvesNumber = number

    # �������� ����� �������� ����������
    def GetCurvesCount(self):
        return self.curvesNumber

    # �������� ����������
    def ClearResults(self):
        self.result_dict = dict()

    def f(self, name, layer = -1):
        rs = self.check(name)
        if rs == None:
            return None

        return rs.GetValue(layer)

    def fmin(self, name):
        rs = self.check(name)
        if rs == None:
            return None
        vl = rs.GetValueList()

        return min(vl)

    def fmax(self, name):
        rs = self.check(name)
        if rs == None:
            return None
        vl = rs.GetValueList()

        return max(vl)

    def flist(self, name):
        rs = self.check(name)
        if rs == None:
            return None
        vl = rs.GetValueList()

        return vl


    def check(self, name):
        self.status = 0
        if name in self.result_dict:
            rs = self.result_dict[name]
            return rs
        else:
            self.status = -1 # ������ �������
            return None