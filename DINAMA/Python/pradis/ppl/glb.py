import af
import math

PI = 3.1415926535897932385
PI180 = PI/180.0
PI2 = PI/2.0
#000000000000001
PI360 = PI*2.0
#1.999999999999999

app = af.Application()
doc = af.Document()
app.New(doc)
root = af.TElement(doc)

sch_main = af.Scheme (root)
sch_main.SetObjectName("MAIN")
sch_main.SetDataList ()
sch_main.SetModelList ()
sch_main.SetImageList ()
sch_main.SetOutVariableList ()
sch_main.SetRunList ()
sch_main.SetPrintList ()
sch_main.SetFragmentList ()
sch_main.SetIncludeList()

sch_list = [sch_main]
sch = sch_list.pop()

el1 = af.TElement (root)
el2 = af.TElement ()
el1.AddElement (el2)
root_list = af.TList (el2)
_scheme_desc = "MAIN"

