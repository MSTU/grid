import af
import glb
import misc
import os
import pradis.multi as multi
import pradis.grid.ModelGrid as MG
import pradis.grid.ModelAnalysis as MA
import pradis.grid.Constants as Constants

class FunctionScanner(multi.FunctionScanner):

    def __init__ (self, nl, pl, desc=misc.default):
        #self.ma = multi.FunctionScanner ()
        vl = pl[0]      #variables list
        rl = pl[1]      #level list or amount of possible variable values. This parameter is unique for each variable
                        #minimal value of this parameter is 2, because each variable has its minimum and maximum value
                        #for example, if you set this parameter for 1st variable in vl to 5 there will be next
                        #possible values of 1st variable: vl[0].Min, vl[0].Max and 3 values with step, that is
                        #calculated as follows (vl[0].Max - vl[0].Min) / (rl[0] - 1)
        fl = pl[2]      #loadcases list

        fl = misc.Expand (fl)

        #if desc != misc.default:
            #self.ma.SetScheme(desc)
        vl = misc.Expand(vl)
        #PVV - Possible Variable Values
        PVV_list = []      #list of PVV
        PVVlists_list = []      #list of PVV lists
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

        if(len(rl) == 1 and len(vl) == 1):
            vl[0].Count = rl[0]
        elif(len(rl) == 1 and len(vl) > 1):
            for i in vl:
                i.Count = rl[0]
        elif(len(rl) == len(vl)):
            n = 0
            for i in vl:
                i.Count = rl[n]
                n += 1
        elif(len(rl) > len(vl)): #ERROR in AmountOfPVV Field
            #Variables Field - field where you specify list of variables,
            #which is used as input parameter for model calculation
            #AmountOfPVV Field - field where you specify list of amounts of PVV for each variable or
            #just one value for all variables
            print "ERROR: You made a mistake in AmountOfPVV Field."
            print "You must enter as many values, as you have in Variables Field."
            print "You can also enter only one value. All variables will get it."
            return Constants.TASK_ERROR
        else: #ERROR in Variables Field (len(vl) > len(rl))
            print "ERROR: You made a mistake in Variables Field"
            print "You must enter as many values, as you have in AmountOfPVV Field."
            print "You can also enter only one value. All variables will get it."
            return Constants.TASK_ERROR

        PVV_list = self.CreatePVVlist(self, vl)

        PVVlists_list.append(PVV_list)

            #pars[var.Name] = var.Value0
            #self.ma.AddVariable (var)
            #n += 1
            #print var

        #for i in fl:
            #self.ma.AddLoadcase (i.lc)
        #c=self.ma.Run()

        misc.SetSolver ("")
        misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")

        #misc.SetPostFile(self.ma.GetHistoryFile())

    def combineVariableValues(self, ma_list, variables_list, PVVlists_list, pars_dict):
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
        if(len(PVVlists_list) == 1):
            #PVVlists_list now contains something like this [[10, 20, 30]],
            #so we're using tempList, which is a simple list: [10, 20, 30]
            tempList = PVVlists_list[0]
            for i in tempList:
                ma = MA.ModelAnalysis()
                pars_tempDict[variables_list[0].Name] = i
                pars_dict.update(pars_tempDict)
                ma.SetParameters(pars_dict)
                ma_list.append(ma)

            return ma_list
        else:
            for j in PVVlists_list[0]:
                pars_tempDict[variables_list[0].Name] = j
                pars_dict.update(pars_tempDict)
                #[1:] removes first list from the PVVlists_list
                self.combineVariableValues(self, ma_list, variables_list[1:], PVVlists_list[1:], pars_dict)

    def CreatePVVlist(self, vl):
        n = 0
        PVV_list = []
        for i in vl:
            i.Step = (i.Max - i.Min) / (i.Count - 1)
            for j in range(i.Min, i.Max, i.Step):
                PVV_list.append(j)

            PVV_list.append(i.Max)

        return PVV_list

    def Run(self, variables_list, loadcases_list, PVVlists_list):
        mg = MG.ModelGrid()
        mg.Init()
        mg.SetLoadcases(loadcases_list)
        ma_list = []        #list of ModelAnalysis objects
        pars_dict = dict()     #parameters dictionary
        #for example: {V1.Name: 1, V2.Name: 0.1, V3.Name: 10}
        ma_list = self.combineVariableValues(self, ma_list, variables_list, PVVlists_list, pars_dict)
        mg.Calculate(ma_list)       #start parallel calculation
        ma_list = mg.WaitAll()      #wait until all calculations are done
