#Block Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import math, random

import urbansimulator as us


class Plot(us.typedSurface):
    #Define and initiate the class
    def __init__(self, srfGUID, blockType):
        us.typedSurface.__init__(self, srfGUID)
        plotAreaMultiplier = (self.Area / 1000)
        if(plotAreaMultiplier < 1):
            plotAreaMultiplier = 1
            height = random.randint(2,3) * 4
        else:
            height = random.randint(1,6) * 4 * plotAreaMultiplier
        
        offsetMultiplier = (self.Area / 2000)
        if(offsetMultiplier < 1):
            offsetMultiplier = 1
        if(offsetMultiplier > 3):
            offsetMultiplier = 3
            
        if(blockType == 4):
            height = random.randint(3,6) * 4
            offsetMultiplier = 1.5
        
        offset = 4 * offsetMultiplier
        
        building = us.Building(self.border, offset, height)
    
    def checkType(self):
        return "Plot"
