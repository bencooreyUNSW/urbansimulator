#Plot Class
#Individual Plot
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import Rhino as rh
import System.Drawing.Color as col

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
        
        
        index = sc.doc.Materials.Add();
        mat = sc.doc.Materials[index]
        mat.DiffuseColor = col.FromArgb(65,65,65);
        mat.CommitChanges();
        
        attr = rh.DocObjects.ObjectAttributes();
        attr.MaterialIndex = index;
        attr.MaterialSource = rh.DocObjects.ObjectMaterialSource.MaterialFromObject;
        
        ext = sc.doc.Objects.AddExtrusion(rg.Extrusion.Create(self.typedSite.border,-2, True), attr)
        sc.doc.Objects.Delete(self.typedSite.GUID, True)
        
        rs.ObjectColor(ext, (65,65,65))
