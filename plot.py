#Block Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us


class Plot(us.typedSurface):
    #Define and initiate the class
    def __init__(self, srfGUID):
        us.typedSurface.__init__(self, srfGUID)
    
    def checkType(self):
        return "Plot"
