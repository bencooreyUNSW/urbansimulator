#Block Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

import urbansimulator as us

import math, random


class Block(us.typedSurface):
    #Define and initiate the class
    def __init__(self, srfGUID, roadNetwork, type):
        us.typedSurface.__init__(self, srfGUID)
        self.srfGuid = srfGUID
        self.roadTrims = roadNetwork.offsetLines
        self.blockSrf = None
        self.plotTrims = None
        self.plots = None
        self.blockType = type
        self.blockTrims = []
        
        self.createBlock()
        self.makePlots()
        
    
    def createBlock(self):
        splitSrfs = us.util.splitSrfwCrvs(self.srfGuid, self.roadTrims,True)
        
        if(splitSrfs == None):
            return False
        listToSort = []
        
        for srf in splitSrfs:
            listToSort.append( [srf, rs.Area(srf)] )
        
        sortedList = sorted(listToSort, key=lambda srf: srf[1], reverse=True)
        
        shrk = rs.ShrinkTrimmedSurface(sortedList[0][0])
        
        self.blockSrf = sortedList[0][0]
        
        for x in range(1,sortedList.Count):
            sc.doc.Objects.Delete(sortedList[x][0], True)
        
        self.cleanup()
    
    def makePlots(self):
        
        self.plotTrims = []
        self.plots = []
        
        if(self.blockType != 3):
            sU = rs.SurfaceDomain(self.blockSrf,0)[0]
            eU = rs.SurfaceDomain(self.blockSrf,0)[1]
            sV = rs.SurfaceDomain(self.blockSrf,1)[0]
            eV = rs.SurfaceDomain(self.blockSrf,1)[1]
            
            pt1V = rs.EvaluateSurface(self.blockSrf,
            us.util.paramAtRemappedDomain(0,sU,eU),
            us.util.paramAtRemappedDomain(0.5,sV,eV))
            
            pt2V = rs.EvaluateSurface(self.blockSrf,
            us.util.paramAtRemappedDomain(1,sU,eU),
            us.util.paramAtRemappedDomain(0.5,sV,eV))
            
            pt1U = rs.EvaluateSurface(self.blockSrf,
            us.util.paramAtRemappedDomain(0.5,sU,eU),
            us.util.paramAtRemappedDomain(0,sV,eV))
            
            pt2U = rs.EvaluateSurface(self.blockSrf,
            us.util.paramAtRemappedDomain(0.5,sU,eU),
            us.util.paramAtRemappedDomain(1,sV,eV))
            
            uLength = rs.Distance(pt1U, pt2U)
            vLength = rs.Distance(pt1V, pt2V)
            
            if(uLength > 60 and vLength > 60):
                if(uLength > vLength):
                    #V is Short Length
                    
                    #construct subdivider
                    divLine = rs.AddLine(pt1U,pt2U)
                    self.blockTrims.append(divLine)
                    
                    self.plotTrims.append(divLine)
                    
                    #construct plot divisions
                    spacing = uLength / 4
                    noDiv = uLength / spacing
                    pts = rs.DivideCurve(divLine, noDiv,False,True)
                    dir = rs.VectorCreate(pt1V, pt2V)
                    
                    
                    for pt in pts:
                        subdLine = rg.Line(pt,dir)
                        moveVec = rg.Transform.Translation(dir * -0.5)
                        subdLine.Transform(moveVec)
                        trimLineGuid = sc.doc.Objects.AddLine(subdLine)
                        self.plotTrims.append(trimLineGuid)
                    
                else:
                    #U is Short Length
                    
                    #construct subdivider
                    divLine = rs.AddLine(pt1V,pt2V)
                    self.plotTrims.append(divLine)
                    
                    #construct plot divisions
                    spacing = uLength / 4
                    noDiv = vLength / spacing
                    pts = rs.DivideCurve(divLine, noDiv,False,True)
                    dir = rs.VectorCreate(pt1U, pt2U)
                    
                    for pt in pts:
                        subdLine = rg.Line(pt,dir)
                        moveVec = rg.Transform.Translation(dir * -0.5)
                        subdLine.Transform(moveVec)
                        trimLineGuid = sc.doc.Objects.AddLine(subdLine)
                        self.plotTrims.append(trimLineGuid)
                        
                splitSrfPlots = us.util.splitSrfwCrvs(self.blockSrf, self.plotTrims,True)
                for srfPlot in splitSrfPlots:
                    shrkSrfPlot = rs.ShrinkTrimmedSurface(srfPlot)
                    self.plots.append( us.Plot(srfPlot, self.blockType))
                    
                    
                    index = sc.doc.Materials.Add();
                    mat = sc.doc.Materials[index]
                    mat.DiffuseColor = col.FromArgb(68,118,67);
                    mat.CommitChanges();
                    
                    attr = rh.DocObjects.ObjectAttributes();
                    attr.MaterialIndex = index;
                    attr.MaterialSource = rh.DocObjects.ObjectMaterialSource.MaterialFromObject;
                    
                    srfToExt = us.typedSurface(srfPlot)
                    
                    ext = sc.doc.Objects.AddExtrusion(rg.Extrusion.Create(srfToExt.border,0.3, True), attr)
                    
                    rs.ObjectColor(ext, (68,118,67))
                    
            else:
                self.blockType = 4 #public building
                self.plots.append( us.Plot(self.blockSrf, self.blockType))
                
                
                index = sc.doc.Materials.Add();
                mat = sc.doc.Materials[index]
                mat.DiffuseColor = col.FromArgb(168,140,54);
                mat.CommitChanges();
                
                attr = rh.DocObjects.ObjectAttributes();
                attr.MaterialIndex = index;
                attr.MaterialSource = rh.DocObjects.ObjectMaterialSource.MaterialFromObject;
                
                srfToExt = us.typedSurface(self.blockSrf)
                
                ext = sc.doc.Objects.AddExtrusion(rg.Extrusion.Create(srfToExt.border,0.3, True), attr)
                theBldSite = sc.doc.Objects.Find(ext)
                theBldSite.Attributes.WireDensity = 0
                theBldSite.CommitChanges()
                
                rs.ObjectColor(theBldSite, (168,140,54))
                
                
                
                
                
        else:
            
            index = sc.doc.Materials.Add();
            mat = sc.doc.Materials[index]
            mat.DiffuseColor = col.FromArgb(149,221,127);
            mat.CommitChanges();
            
            attr = rh.DocObjects.ObjectAttributes();
            attr.MaterialIndex = index;
            attr.MaterialSource = rh.DocObjects.ObjectMaterialSource.MaterialFromObject;
            
            srfToExt = us.typedSurface(self.blockSrf)
            
            ext = sc.doc.Objects.AddExtrusion(rg.Extrusion.Create(srfToExt.border,0.3, True), attr)
            
            thePark = sc.doc.Objects.Find(ext)
            thePark.Attributes.WireDensity = 0
            thePark.CommitChanges()
            
            
            rs.ObjectColor(ext, (149,221,127))
            #theSrf = sc.doc.Objects.Find(self.blockSrf)
            #theSrf.CommitChanges()
            
        
    def cleanup(self):
        sc.doc.Objects.Delete(self.borderGUID, True)
            
    def checkType(self):
        return "Block"