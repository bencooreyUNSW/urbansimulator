import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

#crvsbPlot = rs.DuplicateSurfaceBorder(bPlot)
srfGuids = rs.GetObject("Select Plot Surfaces", rs.filter.surface)
srfGeo = rs.coercesurface(srfGuids)
crv = rs.DuplicateSurfaceBorder(srfGuids)
exCrvs = rs.ExplodeCurves(crv)


class GridVariation:
    
    def __init__(self, srfGuid, srfGeo):
        self.srfGuid = srfGuid
        self.srfGeo = srfGeo

maxLength = 0

listSegments = []

for i in exCrvs:
    listLen = rs.CurveLength(i)
    listSegments.append( [i, listLen] )

sortedListByLength = sorted(listSegments, key=lambda crv: crv[1])

shortestLine1 = sortedListByLength[0][0]
shortestLine2 = sortedListByLength[1][0]
longestLine1 = sortedListByLength[2][0]
longestLine2 = sortedListByLength[3][0]

splitLine = rs.AddLine(rs.CurveMidPoint(shortestLine1), rs.CurveMidPoint(shortestLine2))

divLine1 = rs.DivideCurve(longestLine1, 5, create_points = True)
divLine2 = rs.DivideCurve(longestLine2, 5, create_points = True)
revDivLine2 = divLine2.reverse()


#segSplits = rs.AddLine(rs.coerce3dpoint(divLine1[0,1,2,3,4,5]), rs.coerce3dpoint(divLine2[0, 1, 2, 3, 4, 5]))
sptLine = rs.coerceline(splitLine)



for a in divLine1:
    for b in divLine2:
        line = rs.AddLine(a,b)


print sptLine
print segSplits