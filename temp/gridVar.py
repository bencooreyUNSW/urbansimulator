#Plots Class
#Collection of Plots
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

from util import *

class Plots:
    #Define and initiate the class
    def __init__(self, grid):
        #grid    Grid
        self.grid = grid
        self.plots = []
        self.makePlots()
    
    def makePlots(self):
        for x in range(self.grid.noX):
            plotRows = []
            
            for y in range(self.grid.noY):
                originPt = rg.Point3d( (x*self.grid.spacingX), (y*self.grid.spacingY),0)
                plot = Plot(util.gRect(originPt, self.grid.spacingX, self.grid.spacingY))
                plotRows.append(plot)
                
            self.plots.append(plotRows)
    
    def drawPlots(self):
        for rows in self.plots:
            for item in rows:
                sc.doc.Objects.AddPolyline(item.plotPolyline)
    
    def shadePlots(self):
        for rows in self.plots:
            for item in rows:
                guid = sc.doc.Objects.AddBrep(item.srf)
                theSrf = sc.doc.Objects.Find(guid)
                theSrf.Attributes.WireDensity = 0
                theSrf.CommitChanges()
    
    def drawSegments(self):
        for rows in self.plots:
            for item in rows:
                nBdy = sc.doc.Objects.AddLine(item.nBdy)
                eBdy = sc.doc.Objects.AddLine(item.eBdy)
                wBdy = sc.doc.Objects.AddLine(item.wBdy)
                sBdy = sc.doc.Objects.AddLine(item.sBdy)
                rs.ObjectColor(nBdy,(255,80,0))
                rs.ObjectColor(eBdy,(180,125,0))
                rs.ObjectColor(wBdy,(125,180,0))
                rs.ObjectColor(sBdy,(80,255,0))
                
class GridVariation:
    
    def __init__(self, srfGuid):
        self.srf = srfGuid
        self.srfGeo = rs.coercesurface(self.srf)
        self.Var = []
        self.makeVar()
        
    def getSegments(self):
        crv = rs.ExplodePolysurfaces(self.srfGeo)
        
        #return True
        #for edges in srf:
    def DivLength(self):
        

srfGuids = rs.GetObject("Select Plot Surfaces", rs.filter.surface)
srfGeo = rs.coercesurface(srfGuids)
#myGridVar = GridVariation(srfGuids)

