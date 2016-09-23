#Road Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

from config import *


class typedSegment:
    #Define and initiate the class
    def __init__(self, line, type):
        self.startPt = line.PointAt(0)
        self.endPt = line.PointAt(1)
        self.line = line
        self.length = self.startPt.DistanceTo(self.endPt)
        self.type = type
    
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
            "Invalid Type"
            return False
    
    def offset(self, distance, bothSides):
        theCurve = self.line.ToNurbsCurve()
        curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), distance, sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
        for offset_curve in curves:
            sc.doc.Objects.AddCurve(offset_curve)
            
        if bothSides:
            curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), -distance, sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
            
            for offset_curve in curves:
                sc.doc.Objects.AddCurve(offset_curve)
    
    def checkType(self):
        return "None"
