#Building Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc


class Building:
    #Define and initiate the class
    def __init__(self,plot, offset, height):
        self.plot = plot
        self.offsetPlot = None
        self.offset = offset
        self.height = height
        self.volume = None
        self.construct()
    
    def construct(self):
        theCurve = self.plot.ToNurbsCurve()
        curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), -self.offset, sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
        offsetPlot = rg.Curve.JoinCurves(curves)
        
        for poly in offsetPlot:
            sc.doc.Objects.AddExtrusion(rg.Extrusion.Create(poly,self.height, True))