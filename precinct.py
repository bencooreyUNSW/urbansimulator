#Plot Class
#Individual Plot
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us

import math, random


class Precinct:
    #Define and initiate the class
    def __init__(self, typedSrf, noDiv):
        self.name = "precinct"
        
        self.typedSite  = typedSrf
        self.roadNetwork = us.roadNetwork(typedSrf.borderGUID, noDiv)
        self.Blocks = []
        
        splitSrfs = us.util.splitSrfwCrvs(typedSrf.GUID, self.roadNetwork.cuttingLines,False)
        
        self.noBlock = splitSrfs.Count
        self.pctParks = 0.30
        self.noParks = math.floor(self.noBlock * self.pctParks)
        self.actParks = 0
        
        for srf in splitSrfs:
            if(self.actParks < self.noParks and (random.random() > 0.3)):
                self.Blocks.append( us.Block(srf, self.roadNetwork, 3)) #park
                self.actParks = self.actParks + 1
            else:
                self.Blocks.append( us.Block(srf, self.roadNetwork, random.randint(1,2))) #residential or commercial
        
        #statistics
        self.population = None
        self.noBuildings = None
        self.totalRoadLength = None
        self.gfa = None
        
        self.roadNetwork.cleanup()
        
        rs.ObjectColor(self.typedSite.GUID, (65,65,65))
