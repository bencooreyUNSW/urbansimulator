import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc


#getSrf = rs.GetObject("Select Grid Surfaces", 8)
#rs.sur
#Get Curves
plot = rs.GetObjects("Select Curves",4)

class gridVariation:
    
    def __init__(self, area, offset, degrees):
        self.get_area(area)
        self.set_offset(offset)
        self.set_rotation(degrees)
    
    def get_area(self, area):
        self.a = area
        
    def set_offset(self, crv):
        self.crvDom = rs.CurveDomain(plot)
        print crvDom
        #self.param = (([crvDom[0] + crvDom[1]) / 2)
        

noSeg = rs.CurvePointCount(plot)
print noSeg

#if noSegments = rs.CurvePointCount(plot) == 4:
#print "This is a Rectangle"

def varPlot(crvGuid, delOffsetCrv, skpBadcrvs = True):
    crvs  = rs.coercecurve(crvGuid)
    if crvs == None:
        print ("E001_Invalid Curve")
        if skpBadcrvs == False:
            return False
        crvs.append(validCrv)
    
    if delOffsetCrv:
        sc.doc.Objects.Delete(crvs, True)

def longestLength():
    maxLength = 0
    maxCrvid = None

    for i in exCrvs:
        if rs.CurveLength(i) > maxLength:
            maxLength = rs.CurveLength(i)
            maxCrvid = i


#Area of Closed Curve(plot)
getArea = rs.Area(plot) 
#Centroid of Closed Curve(plot)
ctrPt = rs.CurveAreaCentroid(plot)
centroid = rs.coerce3dpoint(ctrPt)
#Offset of Plot
offset = rs.OffsetCurve(plot, ctrPt[0], 10)
#Exploding Curves to allow Curve extend
ExCrvs = rs.ExplodeCurves(offset)
#Variation for Extend
for crv in ExCrvs:
    crv1 = rs.ExtendCurve(crv, 0, 0, plot)
    crv2 = rs.ExtendCurve(crv1, 0, 1, plot)
    rs.ExtendCurve(
    theCrv = rs.coercecurve(crv1)
    theLine = rs.coerceline(crv1)
    if theLine.Length > 300:
        rot1 = rs.RotateObject(crv1, theCrv.PointAtNormalizedLength(0.5), 10)
    if theLine.Length < 300:
        rot2 = rs.RotateObject(crv1, theCrv.PointAtNormalizedLength(0.2), 10)
    print theLine.Length
    
    
        for curves in :
            extCrv1 = rs.ExtendCurve(curves, 0, 0, plot)
            extCrv2 = rs.ExtendCurve(curves, 0, 1, plot)
        for curves in :
            extCrv1 = rs.ExtendCurve(curves, 0, 0, plot)
            extCrv2 = rs.ExtendCurve(curves, 0, 1, plot)

trim = rs.TrimCurve(crv1, dom)
