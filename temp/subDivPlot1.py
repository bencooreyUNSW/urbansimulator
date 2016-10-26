# Dividing a plot and exploting the plots in the plot and finding the street frontage and rears

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

class subdivPlot:
    def __init__(self, surface, split, vector, length, noDivisions):
        self.get_surface(surface)
        self.to_split(split)
        self.get_vector(u,v)
        self.get_length(length)
        self.create_div()
        
    def get_surface(self,surface):
        self.srf = surface
        self.u = rs.SurfaceDomain(self.srf, 0)
        self.v = rs.SurfaceDomain(self.srf, 1)
    
    def to_split(self, surfacearea):
        self.srfarea = rs.Area(self.srf)
        print self.srfarea
        """
        for self.srf >= 16500:
            return True
            
    
    def get_vector(self, u, v):
        self.row = row
        self.cols = cols
        self.pts = [] 
        
"""
print mySubDiv.split 

Plot = rs.GetObjects("Get Big Plots", 8)
mySubDiv = subdivPlot(plot, )

"""
PlotBBox = rs.BoundingBox(bPlot)
PlotAr = rs.Area(bPlot)
"""
