# Dividing a plot and exploting the plots in the plot and finding the street frontage and rears

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc


bPlot = rs.GetObjects("Get Big Plots", 8)
PlotBBox = rs.BoundingBox(bPlot)
PlotAr = rs.Area(bPlot)

crvsbPlot = rs.DuplicateSurfaceBorder(bPlot)
exCrvs = rs.ExplodeCurves(crvsbPlot)

maxLength = 0

listSegments = []

for i in exCrvs:
    listLen = rs.CurveLength(i)
    listSegments.append( [i, listLen] )

sortedListByLength = sorted(listSegments, key=lambda crv: crv[1])

shortestLine1 = sortedListByLength[0][0]
shortestLine2 = sortedListByLength[1][0]

rs.AddLine(rs.CurveMidPoint(shortestLine1), rs.CurveMidPoint(shortestLine2))

minLength = 100000
minCrvid = None

for i in exCrvs:
    if rs.CurveLength(i) < minLength:
        minLength = rs.CurveLength(i)
        minCrvid = i
print minLength, minCrvid

ctrPt = rs.SurfaceAreaCentroid(bPlot)
crvctrPt = rs.CurveMidPoint(maxCrvid)

pt1 = ctrPt[1]
pt2 = crvctrPt

for i in bPlot:
    midDist1 = rs.Distance(pt1,pt2)

midDiv = rs.OffsetCurve(maxCrvid,ctrPt, midDist)
