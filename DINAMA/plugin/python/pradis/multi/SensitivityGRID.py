import pradis.multi as multi
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

class Sensitivity(multi.ModelLC):

    def __init__ (self, nl, pl, desc = 'FSG'):#desc=misc.default):

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

        self.iteration = 0
        #self.ma.initHistory()


        #		vl0 = self.NormX (self.vl0)
        #		print 'vl0=',self.vl0

        if self.method == 'Forward':
            self.forwback(1.0)
            return

        elif self.method == 'Backward':
            self.forwback(-1.0)

        else:
            print
            print 'Sensitivity Error: method ', self.method, 'is absent'
            print
            return
        #		print 'point2'

        #self.Objective(self.xopt)

    def forwback (self, k):
        self.iteration = 1
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
            if(callable(element)): #if element in criterias list is a callable function
                for i in ma_list:
                    fvalue = element(i)
                    self.fvalue_list.append(fvalue)
            elif(isinstance(element, basestring)): #if element is a string object
                for i in ma_list:
                    lastLayerNumber = i.GetLayerCount()
                    fvalue = i.GetParameterValueFromLayer(element, lastLayerNumber)
                    self.fvalue_list.append(fvalue)
            else:
                print 'ERROR in criterias list'
                return -1

        #calculate derivative matrix
        fx = list()
        for j in range(len(self.fvalue_list) - 1):
            (xa, xb) = self.bounds[j/2]
            dx = self.dx * (xb - xa)
            fx.append((self.fvalue_list[j+1] - self.fvalue_list[j]) / dx)

        k = 0
        der_matrix = empty((len(self.criterias), len(self.variables)))
        for i in range(len(self.criterias)):
            for j in range(len(self.variables)):
                der_matrix[i][j] = fx[k]
                k += 1
        print 'der_matrix:\n'
        print der_matrix

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