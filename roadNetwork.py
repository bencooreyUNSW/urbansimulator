#Network Class
#Transport Network
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import math, random

import urbansimulator as us

class roadNetwork:
    #Define and initiate the class
    def __init__(self,siteBdy, noIterations):
        self.siteBdyGUID = siteBdy
        self.segments = rs.ExplodeCurves(siteBdy)
        self.initialSegment = rs.coercecurve(self.segments[0])
        self.siteBdy = rs.coercecurve(siteBdy)
        
        self.boundaries = []
        self.boundaries.append(self.siteBdyGUID)
        
        self.roadSegments = []
        self.cuttingLines = []
        self.offsetLines = []
        
        self.noIterations = noIterations
        
        self.makeSegments(self.initialSegment, self.boundaries, noIterations, -1, 1)
        
    def perpLineOnCrv(self,crvGeo,t,bdys,dir):
        
        crvNurbs = crvGeo.ToNurbsCurve()
        
        sDom = crvGeo.Domain[0]
        eDom = crvGeo.Domain[1]
        
        rT = (t * (eDom - sDom)) + sDom
        frm = crvNurbs.PerpendicularFrameAt(rT)
        pAxis = -frm[1].XAxis
        
        pt = crvNurbs.PointAt(rT)
        pLine = rg.Line(pt,pAxis,1 * dir)
        
        theInitCrv = sc.doc.Objects.AddLine(pLine)
        extCrv = rs.ExtendCurve(theInitCrv,0,1,bdys)
        
        
        return extCrv
    
    def makeSegments(self, crv, boundaries, cnt, dir, roadType):
        if cnt > 0:
            
            t = (random.random() * 0.5) + 0.25
            newSegment = self.perpLineOnCrv(crv, t, self.boundaries, dir)
            
            newSegmentGeo = rs.coercecurve(newSegment)
            self.boundaries.append(newSegment)
            
            theRoad = us.Road(newSegmentGeo,roadType)
            theRoad.offsetCurve(True)
            
            self.cuttingLines.append(newSegment)
            self.roadSegments.append(theRoad)
            
            for oC in theRoad.offsetCrvs:
                self.offsetLines.append(oC)
            
            self.makeSegments(newSegmentGeo, self.boundaries, cnt - 1, 1, roadType + 1)
            self.makeSegments(newSegmentGeo, self.boundaries, cnt - 1, -1, roadType + 1)
            
    def draw(self):
        for road in self.roadSegments:
            sc.doc.Objects.AddCurve(road.line)
    
    def cleanup(self):
        for delLine in self.cuttingLines:
            sc.doc.Objects.Delete(delLine, True)