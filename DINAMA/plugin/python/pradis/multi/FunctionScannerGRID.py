#import af
#import glb
#import misc
import os
import pradis.multi as multi
import grid.ModelGrid as MG
import grid.ModelAnalysis as MA
from numpy import linspace
import grid.Constants as Constants

class FunctionScanner():

    def __init__ (self, nl, pl, desc='FSG'):#misc.default):
        #self.ma = multi.FunctionScanner ()
        self.variables = pl[0]      #variables list
        self.var_levels = pl[1]
        #level list or amount of possible variable values. This parameter is unique for each variable
        #minimal value of this parameter is 2, because each variable has its minimum and maximum value
        #for example, if you set this parameter for 1st variable in self.variables to 5 there will be next
        #possible values of 1st variable: self.variables[0].Min, self.variables[0].Max and 3 values with step, that is
        #calculated as follows: (self.variables[0].Max - self.variables[0].Min) / (self.var_levels[0] - 1)
        self.loadcases = pl[2]      #loadcases list
        #PVV - Possible Variable Values
        self.PVV_arrays_list = list()      #list of 1-dimensional numpy arrays. Each array contains PVV

        #fl = misc.Expand (fl)

        #if desc != misc.default:
            #self.ma.SetScheme(desc)
        #vl = misc.Expand(vl)
        '''
        for i in vl:
            var = multi.Variable()
            var.Name = i.Name
            var.Value0 = i.Value0
            if(i.Min != None):
                var.Min = i.Min
            else:
                var.Min = i.Value0
            if(i.Max != None):
                var.Max = i.Max
            else:
                var.Max = i.Value0
            if(n < len(rl)):
                var.Count = rl[n]
            else:
                var.Count = 1
            var.Step = (var.Max - var.Min) / (var.Count - 1)
            for j in range(var.Min, var.Max, var.Step):
                PVV_list.append(j)
            PVV_list.append(var.Max)
            PVVlists_list.append(PVV_list)

            #pars[var.Name] = var.Value0
            #self.ma.AddVariable (var)
            n += 1
            #print var
        '''

        if(len(self.var_levels) == 1 and len(self.variables) == 1):
            self.variables[0].Count = self.var_levels[0]
        elif(len(self.var_levels) == 1 and len(self.variables) > 1):
            for i in self.variables:
                i.Count = self.var_levels[0]
        elif(len(self.var_levels) == len(self.variables)):
            n = 0
            for i in self.variables:
                i.Count = self.var_levels[n]
                n += 1
        elif(len(self.var_levels) > len(self.variables)): #ERROR in AmountOfPVV Field
            #Variables Field - field where you specify list of variables,
            #which is used as input parameter for model calculation
            #AmountOfPVV Field - field where you specify list of amounts of PVV for each variable or
            #just one value for all variables
            raise RuntimeError("You made a mistake in AmountOfPVV Field. " +
            "You must enter as many values, as you have in Variables Field. " +
            "You can also enter only one value. All variables will get it. ")
        else: #ERROR in Variables Field (len(self.variables) > len(self.var_levels))
            raise RuntimeError("You made a mistake in Variables Field " +
            "You must enter as many values, as you have in AmountOfPVV Field. " +
            "You can also enter only one value. All variables will get it.")

        self.PVV_arrays_list = self.CreateListOfPVVArrays(self.variables)

            #pars[var.Name] = var.Value0
            #self.ma.AddVariable (var)
            #n += 1
            #print var

        #for i in fl:
            #self.ma.AddLoadcase (i.lc)
        #c=self.ma.Run()

        #misc.SetSolver ("")
        #misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")

        #misc.SetPostFile(self.ma.GetHistoryFile())

    def CreateListOfPVVArrays(self, vl):
        #PVV_array = empty(1)        #1-d array (it contains garbage yet)
        PVV_arrays_list = list()
        for i in vl:
            PVV_array = linspace(i.Min, i.Max, i.Count)
            PVV_arrays_list.append(PVV_array)
        return PVV_arrays_list

    '''
    def combineVariableValues(self, ma_list, variables_list, PVVlists_list, pars_dict, flag):
        #ma_list - list of ModelAnalysis objects, each with a dictionary that contains
        #names of variables and their values. For example: {V1.Name: 1, V2.Name: 0.1, V3.Name: 10}

        #variables_list - list that contains variable objects
        #for example: [V1, V2, V3]

        #PVVlists_list - list that contains lists of PVV (Possible Variable Values)
        #for example: [[1, 2, 3, 4], [0.1, 0.2, 0.3], [10, 20, 30]]
        #PVV of Variable1: [1, 2, 3, 4]
        #PVV of Variable2: [0.1, 0.2, 0.3]
        #PVV of Variable3: [10, 20, 30]

        #pars_dict - parameters dictionary
        pars_tempDict = dict()
        print "pervoe:"
        print ma_list
        if(len(PVVlists_list) == 1):
            #PVVlists_list now contains something like this [[10, 20, 30]],
            #so we're using tempList, which is a simple list: [10, 20, 30]
            tempList = PVVlists_list[0]
            for i in tempList:
                print 'v if'
                ma = MA.ModelAnalysis()
                pars_tempDict[variables_list[0].Name] = i
                pars_dict.update(pars_tempDict)
                ma.SetParameters(pars_dict)
                print 'posle set'
                print ma
                print ma.GetParameters()
                ma_list.append(ma)
                print 'posle append:'
                for i in ma_list:
                    print i
            if(flag == True):
                print 'vne tsikla'
                for i in ma_list:
                    print i.GetParameters()
                return ma_list
                #print pars_dict
        else:
            for j in PVVlists_list[0]:
                print 'v else'
                if(j == PVVlists_list[0][variables_list[0].Count - 1]):
                    flag = True
                pars_tempDict[variables_list[0].Name] = j
                pars_dict.update(pars_tempDict)
                #[1:] removes first list from the PVVlists_list
                self.combineVariableValues(ma_list, variables_list[1:], PVVlists_list[1:], pars_dict, flag)
    '''

    def all_combinations(self, list_of_lists):
        if(len(list_of_lists) > 1):
            result_list = list()
            combinations_without_first_list = self.all_combinations(list_of_lists[1:])
            for item in list_of_lists[0]:
                for combination in combinations_without_first_list:
                    if type(combination) is list:
                        result_list.append([item] + combination)
                    else:
                        result_list.append([item] + [combination])
            return result_list
        else:
            return list_of_lists[0]

    def map_list_to_dict(self, combination, keys):
        result = dict()
        if(len(keys) > 1):
            for i in xrange(len(combination)):
                result[keys[i].Name] = combination[i]
        else:
            result[keys[0].Name] = combination

        return result

    def Run(self):
        mg = MG.ModelGrid()
        mg.Init()
        mg.SetLoadcases(self.loadcases)
        ma_list = []        #list of ModelAnalysis objects
        PVV_arrays_list = self.CreateListOfPVVArrays(self.variables)
        if(len(PVV_arrays_list) > 1):
            all_combs = self.all_combinations(PVV_arrays_list)
        else:
            all_combs = PVV_arrays_list[0]
        in_dicts = [self.map_list_to_dict(combination, self.variables) for combination in all_combs]
        for dic in in_dicts:
            ma = MA.ModelAnalysis()
            ma.SetParameters(dic)
            ma_list.append(ma)

        mg.Calculate(ma_list)       #start parallel calculation
        ma_list = mg.WaitAll()      #wait until all calculations are done
