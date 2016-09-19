#Utilities Class
#Set of static functions that can be used
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

class util:
    
    #Create rectangle from corner with width and height
    @staticmethod
    def gRect(origin,width, height):
        #origin     point3d
        #width     double
        #height    double
        return rg.Rectangle3d(rg.Plane(origin, rg.Vector3d(0,0,1)), width,height)
        
    #Create rectangle from corner with width and height
    @staticmethod
    def filletCurves(curve1,curve2):
        #origin     point3d
        #width     double
        #height    double
        return rg.Rectangle3d(rg.Plane(origin, rg.Vector3d(0,0,1)), width,height)