import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

crvs = rs.GetObjects("Select Curves",4)

actualCrvs = []

rs.EnableRedraw(False)

for crv in crvs:
    theCrv = rs.coercecurve(crv)
    actualCrvs.append(theCrv)
    midPt = theCrv.PointAtNormalizedLength(0.5)
    sc.doc.Objects.AddPoint(midPt)
    
rs.EnableRedraw(True)
