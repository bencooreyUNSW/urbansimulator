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
            1: 1, #Primary Street Frontage
            2: 2, #Secondary Street Frontage
            3: 3  #Tertiary Street Frontage
        }
        
        if(type > 0 and type < switcher.Count):
            return switcher.get(type, 0)
    
    def checkType(self):
        return "Block Boundary"
