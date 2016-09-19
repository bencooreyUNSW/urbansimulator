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
        self.plotPolyline = None
        self.srf = None
        self.segments = None
        
        self.guid = None
        self.bdySegments = []
        self.extractBoundaries()
        self.shade()
    
    def extractBoundaries(self):
        self.plotPolyline = self.rect.ToPolyline()
        self.segments = self.plotPolyline.GetSegments()
        if(len(self.segments) == 4):
            self.bdySegments.append(bdySegment(self.segments[0],1))
            self.bdySegments.append(bdySegment(self.segments[1],3))
            self.bdySegments.append(bdySegment(self.segments[2],4))
            self.bdySegments.append(bdySegment(self.segments[3],3))
       
    def shade(self):
        self.srf = rg.Brep.CreatePlanarBreps(self.plotPolyline.ToNurbsCurve())[0]