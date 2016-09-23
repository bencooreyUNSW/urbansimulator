#Block Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us


class Block(us.typedSurface):
    #Define and initiate the class
    def __init__(self, srfGUID, roadNetwork):
        us.typedSurface.__init__(self, srfGUID)
        self.roadTrims = roadNetwork.offsetLines
        self.blockSrf = None
        
        splitSrfs = us.util.splitSrfwCrvs(srfGUID, self.roadTrims,True)
        
        listToSort = []
        
        for srf in splitSrfs:
            listToSort.append( [srf, rs.Area(srf)] )
        
        sortedList = sorted(listToSort, key=lambda srf: srf[1])
        
        self.blockSrf = sortedList[sortedList.Count]
        
        for x in range(0,sortedList.Count-1):
            sc.doc.Objects.Delete(sortedList[x][0], True)
        
        print(splitSrfs)
    
    def checkType(self):
        return "Block"
