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
            1: 10, #Primary Road
            2: 6, #Secondary Road
            3: 3, #Tertiary Road
        }
        
        if(type > 0 and type < switcher.Count):
            return switcher.get(type, 0)
        else:
            return switcher.get(type, 3)
    
    def checkType(self):
        return "Road"
