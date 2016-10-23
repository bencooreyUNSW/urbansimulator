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
        self.siteBdy = rs.coercecurve(siteBdy)
        
        self.boundaries = []
        self.boundaries.append(self.siteBdyGUID)
        
        self.roadSegments = []
        self.cuttingLines = []
        self.offsetLines = []
        
        self.noIterations = noIterations
        self.startT = random.random()
        self.startT = 0.2
        
        self.makeSegments(self.siteBdy, self.boundaries, noIterations)
        
    def perpLineOnCrv(self,crvGeo,t,bdys):
        
        #rs.EnableRedraw(False)
        crvNurbs = crvGeo.ToNurbsCurve()
        
        sDom = crvGeo.Domain[0]
        eDom = crvGeo.Domain[1]
        
        rT = (t * (eDom - sDom)) + sDom
        frm = crvNurbs.PerpendicularFrameAt(rT)
        pAxis = -frm[1].XAxis
        
        pt = crvNurbs.PointAt(rT)
        pLine = rg.Line(pt,pAxis,-50)
        
        theInitCrv = sc.doc.Objects.AddLine(pLine)
        extCrv = rs.ExtendCurve(theInitCrv,0,1,bdys)
        
        #sc.doc.Objects.Delete(extCrv,True) #cleanup
        #rs.EnableRedraw(True)
        return extCrv
    
    def makeSegments(self, crv, boundaries, cnt):
        if cnt > 0:
            
            newSegment = self.perpLineOnCrv(crv, self.startT, self.boundaries)
            
            newSegmentGeo = rs.coercecurve(newSegment)
            self.boundaries.append(newSegment)
            
            theRoad = us.Road(newSegmentGeo,1)
            theRoad.offsetCurve(True)
            
            self.cuttingLines.append(newSegment)
            self.roadSegments.append(theRoad)
            
            for oC in theRoad.offsetCrvs:
                self.offsetLines.append(oC)
            
            self.makeSegments(newSegmentGeo, self.boundaries, cnt - 1)
            
    def draw(self):
        for road in self.roadSegments:
            sc.doc.Objects.AddCurve(road.line)
            