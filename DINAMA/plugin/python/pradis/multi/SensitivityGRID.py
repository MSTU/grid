#import pradis.multi as multi
import grid.ModelGrid as MG
import grid.ModelAnalysis as MA
import grid.Constants as Constants
from numpy import empty
#import af
#import glb
#import misc
import os
import math

#import scipy

from numpy import copy



MaxValue = 1e36

class Sensitivity():

    def __init__ (self, nl, pl, desc = 'SG'):#desc=misc.default):

        #self.ma = multi.ModelLC ()

        self.method = pl[0]         #forward or backward analysis
        self.variables = pl[1]      #variables list
        self.loadcases = pl[2]      #loadcases list
        self.criterias = pl[3]      #criterias list
        self.dx = pl[4]             #relative step ( 0 < self.dx < 1)

        #if desc != misc.default:
            #self.ma.SetScheme(desc)
            #self.ma.SetDescription('Sensitivity: '+desc)

        #self.loadcases = misc.Expand (self.loadcases)

        #for i in self.loadcases:
            #self.ma.AddLoadcase (i.lc)

        #self.variables = misc.Expand(self.variables)
        #self.criterias = misc.Expand(self.criterias)

        self.fvalue_list = []
        self.vl0 = []
        self.bounds = []
        for i in self.variables:
            #self.ma.AddParameter (i.Name)
            #self.ma.AddExtParameter (i.Name)
            self.vl0.append (i.Value0)
            self.bounds.append((i.Min, i.Max))

        #		self.createNormX()

        #self.addCriteryHistory()

        #self.Run()
        #misc.SetSolver ("")
        #misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")

        #misc.SetPostFile(self.ma.GetHistoryFile())

    def Run (self):
        #self.iteration = 0
        #self.ma.initHistory()


        #		vl0 = self.NormX (self.vl0)
        #		print 'vl0=',self.vl0

        if(self.method == 'Forward'):
            self.forwback(1.0)
            return
        elif(self.method == 'Backward'):
            self.forwback(-1.0)
        else:
            print
            print 'Sensitivity Error: method ', self.method, 'is absent'
            print
            return
        #		print 'point2'

        #self.Objective(self.xopt)

    def forwback(self, k):
        #self.iteration = 1
        mg = MG.ModelGrid()
        mg.Init()
        mg.SetLoadcases(self.loadcases)
        ma_list = list()

        j = 0
        for i in self.variables:
            ma1 = MA.ModelAnalysis()
            ma2 = MA.ModelAnalysis()
            par_dict = dict()
            par_dict[i.Name] = i.Value0
            ma1.SetParameters(par_dict)
            par_dict.clear()
            ma_list.append(ma1)

            (xa, xb) = self.bounds[j]
            par_dict[i.Name] = i.Value0 + k * self.dx * (xb - xa)
            ma2.SetParameters(par_dict)
            ma_list.append(ma2)
            j += 1

        #for i in ma_list:
            #print i.GetParameters()
        mg.Calculate(ma_list)
        ma_list = mg.WaitAll()

        self.Criteria(ma_list)

    '''
        #self.ma.SetFilePostfix ('_sen')
        self.iteration = 1
        j = 0
        x = self.vl0
        #		print 'point3:', x, 'vl0=', self.vl0, 'x_=', x_

        for i in x:
            self.ma.SetParameterValue (j, str(i))
            self.ma.SetExtParameterValue (j, str(i))
            j += 1
        len = j

        # first analysis

        #c = self.ma.Run()
        #if c != 0:
            #print 'Sensitivity: Error code = ', c

        self.Criteria(x)

        #self.ma.writeHistory(self.iteration)

        # other analyses
        for ii in range (0, len):
            self.iteration += 1
            x = []
            for i in self.vl0:
                x.append(i)
            (xa, xb) = self.bounds[ii]
            x[ii] = x[ii] + k*self.dx*(xb-xa)
            j = 0
            for i in x:
                self.ma.SetParameterValue (j, str(i))
                self.ma.SetExtParameterValue (j, str(i))
                j = j+1

            c = self.ma.Run()
            if c != 0:
                print 'Sensitivity: Error code = ', c

            self.Criteria(x)
            self.ma.writeHistory(self.iteration)
    '''

    def Criteria(self, ma_list):
        for element in self.criterias:
            if(callable(element)): #if element in criterias list is a callable user function
                for i in ma_list:
                    fvalue = element(i)
                    self.fvalue_list.append(fvalue)
            elif(isinstance(element, basestring)): #if element is a string object
                for i in ma_list:
                    lastLayerNumber = i.GetLayerCount()
                    fvalue = i.GetValueFromLayerByName(element, lastLayerNumber)
                    self.fvalue_list.append(fvalue)
            else:
                print 'ERROR in criterias list'
                return -1
        #here is an instance
        #variables: V1, V2
        #criterias: C1, C2
        #method: Forward
        #in fvalue_list we have: [C1V1, C1V1_dx, C2V2, C2V2_dx],
        #where C1V1 and C2V2 are function's values in V1.Value0 and V2.Value0 points accordingly
        #C1V1_dx and C2V2_dx are function's values in V1.Value + step and V2.Value0 + step points accordingly
        #step = self.dx * (V#.xb - V#.xa), where # is variable number (# = 1 or 2)
        f_x_list = self.fvalue_list[0::2]
        f_x_dx_list = self.fvalue_list[1::2]
        #in f_x_list we have only values in V.Value0 points
        #in our example they are: [C1V1, C2V2]
        #in f_x_dx_list we have only values in V.Value0 + step points
        #in our example they are: [C1V1_dx, C2V2_dx]
        if(self.method == 'Forward'):
            dfx_list = [f_x_dx - f_x for f_x_dx, f_x in zip(f_x_dx_list, f_x_list)]
        else:
            dfx_list = [f_x - f_x_dx for f_x_dx, f_x in zip(f_x_dx_list, f_x_list)]
        #in forward method we're using forward difference: (f(x + dx) - f(x)) / dx
        #in backward method we're using backward difference: (f(x) - f(x - dx)) / dx
        dx_list = [self.dx * (xb - xa) for xa, xb in [] + self.bounds * (len(self.criterias))]
        #dx_list is a list of calculated steps
        der_fx_list = [dfx / dx for dfx, dx in zip(dfx_list, dx_list)]
        #der_fx_list is are list of calculated derivatives which are calculated as dfx / dx
        #in our example this list contains of: [dC1/dV1, dC1/dV2, dC2/dV1, dC2/dV2]

        #create derivative matrix
        k = 0
        der_matrix = empty((len(self.criterias), len(self.variables)))
        for i in range(len(self.criterias)):
            for j in range(len(self.variables)):
                der_matrix[i][j] = der_fx_list[k]
                k += 1
        #derivative matrix has a similar structure as Jacobian matrix:
        #dC1/dV1    dC1/dV2
        #dC2/dV1    dC2/dV2

        print "f_x_dx_list: " + str(f_x_dx_list)
        print "f_x_list: " + str(f_x_list)
        print "dfx_list: " + str(dfx_list)
        print "dx_list: " + str(dx_list)
        print "der_fx_list: " + str(der_fx_list)
        print 'der_matrix: ' + str(der_matrix)

        '''
        j = len(self.vl0)
        ii = 0

        for constraints in self.criterias:
            r = constraints(x, self.ma)
            self.ma.SetExtParameterValue (j, str(r))

            self.fvalue.append(r);
            j += 1
            ii += 1

        #			print self.fvalue

        #		print 'debug:criteria.1'

        #		j = len(self.vl0) + len (self.fce)+1
        ii = 0
        for constraints in self.criterias:
            if (self.iteration==1):
                self.ma.SetExtParameterValue (j, '0.0')
            else:
                (xa, xb) = self.bounds[self.iteration-2]
                dx = self.dx*(xb-xa)
                fx = (self.fvalue[len (self.criterias)*(self.iteration-1)+ii]-self.fvalue[ii])/dx

                #				print 'ii=',len (self.fce)*(self.iteration-1)+ii,' jj=',ii

                self.ma.SetExtParameterValue(j, str(fx))
            ii += 1
            j  += 1
        '''