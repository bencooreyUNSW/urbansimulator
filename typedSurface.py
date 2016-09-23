#Plot Class
#Individual Plot
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us


class typedSurface:
    #Define and initiate the class
    def __init__(self, srfGUID):
        self.GUID = srfGUID
        self.borderGUID = rs.DuplicateSurfaceBorder(srfGUID)
        self.srfGeo = rs.coercesurface(srfGUID)
        self.brep = self.srfGeo.ToBrep()
        self.edgeCrvs = self.brep.DuplicateEdgeCurves()
        self.border = rg.Curve.JoinCurves( self.edgeCrvs )[0]
        self.nurbsCrv = self.border.ToNurbsCurve()
        
        amp = rg.AreaMassProperties.Compute(self.nurbsCrv, us.util.tol() )
        self.Centroid = amp .Centroid
        self.Area = amp.Area
        
    def checkType(self):
        return "Generic"