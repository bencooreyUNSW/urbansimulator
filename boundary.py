#Road Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us

class Boundary(us.typedSegment):
    #Define and initiate the class
    def __init__(self, line, type):
        us.typedSegment.__init__(self,line,type)
        
    def offsetWidth(self, type):
        switcher = {
            1: 6, #Primary Street Frontage
            2: 3, #Secondary Street Frontage
            3: 1.5, #Sides
            4: 4, #Rear
        }
        
        if(type > 0 and type < switcher.Count):
            return switcher.get(type, 0)
    
    def checkType(self):
        return "Boundary"
