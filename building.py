#Building Class
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino as rh
import scriptcontext as sc
import System.Drawing.Color as col




class Building:
    #Define and initiate the class
    def __init__(self,plot, offset, height):
        self.plot = plot
        self.offsetPlot = None
        self.offset = offset
        self.height = height
        self.volume = None
        self.construct()
    
    def construct(self):
        theCurve = self.plot.ToNurbsCurve()
        curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), -self.offset, sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
        offsetPlot = rg.Curve.JoinCurves(curves)
        
        for poly in offsetPlot:
            
            colour = (167,204,46) #grass
            
            if(self.height < 4):
                colour = (18,69,222) #R2
            if(self.height >= 4):
                colour = (149,103,182) #R4
            if(self.height >= 18):
                colour = (204,94,170) #R6
            if(self.height >= 24):
                colour = (242,151,169) #R8
            if(self.height >= 36):
                colour = (238,96,70) #R12
            if(self.height >= 75):
                colour = (250,170,27) #R25
            if(self.height >= 105):
                colour = (253,229,45) #R35+
            
            
            index = sc.doc.Materials.Add();
            mat = sc.doc.Materials[index]
            mat.DiffuseColor = col.FromArgb(colour[0],colour[1],colour[2]);
            mat.CommitChanges();
            
            attr = rh.DocObjects.ObjectAttributes();
            attr.MaterialIndex = index;
            attr.MaterialSource = rh.DocObjects.ObjectMaterialSource.MaterialFromObject;
            
            theBuildingExt = sc.doc.Objects.AddExtrusion(rg.Extrusion.Create(poly,self.height, True), attr)
            
            theBldObj = sc.doc.Objects.Find(theBuildingExt)
            rs.ObjectColor(theBldObj, colour)
            