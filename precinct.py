#Plot Class
#Individual Plot
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us


class Precinct:
    #Define and initiate the class
    def __init__(self, typedSrf):
        self.name = "precinct"
        
        self.typedSite  = typedSrf
        self.roadNetwork = us.roadNetwork(typedSrf.borderGUID, 2 )
        self.Blocks = []
        
        splitSrfs = us.util.splitSrfwCrvs(typedSrf.GUID, self.roadNetwork.cuttingLines,False)
        
        for srf in splitSrfs:
            self.Blocks.append( us.Block(srf, self.roadNetwork) )
        
        #statistics
        self.population = None
        self.noBuildings = None
        self.totalRoadLength = None
        self.gfa = None