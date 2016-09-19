#Plot Class
#Individual Plot
#Contributors: Ben Coorey

import Rhino.Geometry as rg
import scriptcontext as sc

from bdySegment import *

class Plot:
    #Define and initiate the class
    def __init__(self, rect):
        #rect    Rectangle3D
        self.rect = rect
        self.plotPolyline = self.rect.ToPolyline()
        self.srf = None
        self.segments = None
        self.guid = None
        self.bdySegments = []
        self.extractBoundaries()
        self.shade()
        tol = sc.doc.ModelAbsoluteTolerance
        mp = rg.AreaMassProperties.Compute(self.plotPolyline.ToNurbsCurve(), tol)
        self.Centroid = mp.Centroid
        self.Area = mp.Area
        #sc.doc.Objects.AddPoint(self.Centroid)
    
    def extractBoundaries(self):
        self.segments = self.plotPolyline.GetSegments()
        if(len(self.segments) == 4):
            self.bdySegments.append(bdySegment(self.segments[0],1))
            self.bdySegments.append(bdySegment(self.segments[1],3))
            self.bdySegments.append(bdySegment(self.segments[2],4))
            self.bdySegments.append(bdySegment(self.segments[3],3))
       
    def shade(self):
        self.srf = rg.Brep.CreatePlanarBreps(self.plotPolyline.ToNurbsCurve())[0]