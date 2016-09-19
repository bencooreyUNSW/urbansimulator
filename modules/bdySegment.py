#bdySegment Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

from config import *


class bdySegment:
    #Define and initiate the class
    def __init__(self, line, type):
        self.startPt = line.PointAt(0)
        self.endPt = line.PointAt(1)
        self.line = line
        self.length = line.Length
        self.type = type
    
    def offsetBdy(self):
        theCurve = self.line.ToNurbsCurve()
        curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), config.bdyOffset(self.type), sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
        
        for offset_curve in curves:
            sc.doc.Objects.AddCurve(offset_curve)
