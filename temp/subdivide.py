import rhinoscriptsyntax as rs
import Rhino as rh


outline = rs.GetObject("Select closed polyline to build surface", 4)
srf = rs.AddPlanarSrf(outline)

bb = rs.BoundingBox(srf)


#exoutline = rs.ExplodeCurves(outline)
#rs.OffsetCurve(exoutline, 
#rs.ExtendCurveLength(

