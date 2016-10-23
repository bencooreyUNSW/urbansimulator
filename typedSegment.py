#Road Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us

class typedSegment:
    #Define and initiate the class
    def __init__(self, lineGeo, type):
        self.startPt = lineGeo.PointAt(0)
        self.endPt = lineGeo.PointAt(1)
        self.line = lineGeo
        self.nurbsCrv = lineGeo.ToNurbsCurve()
        self.length = self.startPt.DistanceTo(self.endPt)
        self.type = type
        self.offsetCrvs = []
    
    def offsetWidth(self, type):
        switcher = {
            1: 3, #TypeA
            2: 2, #TypeB
            3: 1, #TypeC
        }
        
        if(type > 0 and type < switcher.Count):
            return switcher.get(type, 0)
    
    def offsetCurve(self,bothSides):
        if self.offsetWidth(self.type) != None:
            self.offset( self.offsetWidth(self.type), 1)
        else:
            return False
    
    def offset(self, distance, bothSides):
        
        curves = self.nurbsCrv.Offset(us.util.xyPlane(), distance, us.util.tol(), rg.CurveOffsetCornerStyle.None)
        for offset_curve in curves:
            self.offsetCrvs.append(offset_curve)
            
        if bothSides:
            curves = self.nurbsCrv.Offset(us.util.xyPlane(), -distance, us.util.tol(), rg.CurveOffsetCornerStyle.None)
            for offset_curve in curves:
                self.offsetCrvs.append(offset_curve)
    
    def checkType(self):
        return "Generic"
