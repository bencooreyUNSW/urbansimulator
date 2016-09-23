#Road Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us


class Road(us.typedSegment):
    #Define and initiate the class
    def __init__(self, line, type):
        us.typedSegment.__init__(self,line,type)
    
    def offsetWidth(self, type):
        switcher = {
            1: 8, #Primary
            2: 6, #Secondary
            3: 4, #Tertiary
        }
        
        if(type > 0 and type < switcher.Count):
            return switcher.get(type, 0)
    
    def checkType(self):
        return "Road"
