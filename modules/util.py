#Utilities Class
#Set of static functions that can be used
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

class util:
    
    #Create rectangle from corner with width and height
    @staticmethod
    def gRect(origin,width, height):
        #origin     point3d
        #width     double
        #height    double
        return rg.Rectangle3d(rg.Plane(origin, rg.Vector3d(0,0,1)), width,height)
        
    #Create rectangle from corner with width and height
    @staticmethod
    def filletCurves(curve1,curve2):
        #origin     point3d
        #width     double
        #height    double
        return rg.Rectangle3d(rg.Plane(origin, rg.Vector3d(0,0,1)), width,height)
        
    #Split surface with Curves
    #Contributor: Ben Coorey
    @staticmethod
    def splitSrfwCrvs(srfGuid, crvGuids, delOrigSrf, delOrigCrvs, skipBadCrvs = True):
        """Split a Surface with a Set of Curves
        Parameters:
          srfGuid: the input surface ID
          crvsGuid: the input trimming curves ID
          skipBadCrvs: flag to omit bad curves or fail the script if bad curves encountered
          delOrigSrf: flag to Delete the Original Surface
          delOrigCrvs: Flag to Delete the Original Trimming Curves
        Returns:
          True if successful
          False if not successful
        """
        srf = rs.coercesurface(srfGuid)
        if srf == None:
            print("SSC001_Not a Valid Surface")
            return False
            
        crvs = []
        for crv in crvGuids:
            validCrv = rs.coercecurve(crv)
            if validCrv == None:
                print("SSC002_Not a Valid Curve")
                if skipBadCrvs == False:
                    return False
            crvs.append(validCrv)
        
        #Have a Valid Surface and Valid Curves
        
        splitSrf = rg.BrepFace.Split(srf,crvs,0.1)
        polySrf = sc.doc.Objects.AddBrep(splitSrf)
        splitSrfs = rs.ExplodePolysurfaces(polySrf)
        
        #Change Isocurve Density to 0 for Individual Split Surfaces
        for srf in splitSrfs:
            theSrf = sc.doc.Objects.Find(srf)
            theSrf.Attributes.WireDensity = 0
            theSrf.CommitChanges()
        
        if delOrigSrf:
            sc.doc.Objects.Delete(srfGuid, True)
        
        if delOrigCrvs:
            for crv in crvGuids:
                sc.doc.Objects.Delete(crv,True)
        
        sc.doc.Objects.Delete(polySrf, True)