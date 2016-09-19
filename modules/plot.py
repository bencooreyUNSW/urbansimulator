#Plot Class
#Individual Plot
#Contributors: Ben Coorey

import Rhino.Geometry as rg
import scriptcontext as sc

class Plot:
    #Define and initiate the class
    def __init__(self, rect):
        #rect    Rectangle3D
        self.rect = rect
        self.plotPolyline = None
        self.srf = None
        self.segments = None
        self.nBdy = None
        self.guid = None
        self.sBdy = None
        self.wBdy = None
        self.eBdy = None
        self.extractBoundaries()
        self.shade()
    
    def extractBoundaries(self):
        self.plotPolyline = self.rect.ToPolyline()
        self.segments = self.plotPolyline.GetSegments()
        if(len(self.segments) == 4):
            self.sBdy = self.segments[0]
            self.eBdy = self.segments[1]
            self.nBdy = self.segments[2]
            self.wBdy = self.segments[3]
            
    def shade(self):
        self.srf = rg.Brep.CreatePlanarBreps(self.plotPolyline.ToNurbsCurve())[0]