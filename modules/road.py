#Road Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

from config import *


class Road:
    #Define and initiate the class
    def __init__(self, line, type):
        self.startPt = line.PointAt(0)
        self.endPt = line.PointAt(1)
        self.line = line
        self.length = line.Length
        self.type = type
    
    def drawRoad(self, withOffsets):
        #construct line and add to document
        
        #withOffsets - 0 or 1
        sc.doc.Objects.AddLine(self.line)
        
        if withOffsets:
            theCurve = self.line.ToNurbsCurve()
            curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), config.roadWidth(self.type), sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
            
            for offset_curve in curves:
                sc.doc.Objects.AddCurve(offset_curve)
