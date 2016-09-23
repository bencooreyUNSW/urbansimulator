#Utilities Class
#Set of static functions that can be used
#Contributors: Ben Coorey

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc

import math, random

import urbansimulator as us

class util:
    
    @staticmethod
    def xyPlane():
        return rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1))
    
    @staticmethod
    def tol():
        return sc.doc.ModelAbsoluteTolerance
    
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
    def splitSrfwCrvs(srfGuid, crvGuids, delOrigSrf, skipBadCrvs = True):
        """Split a Surface with a Set of Curves
        Parameters:
          srfGuid: the input surface ID
          crvsGuid: the input trimming curves ID
          skipBadCrvs: flag to omit bad curves or fail the script if bad curves encountered
          delOrigSrf: flag to Delete the Original Surface
        Returns:
          True if successful
          False if not successful
        """
        
        retSrf = []
        
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
        retSrf = splitSrfs
        
        #Change Isocurve Density to 0 for Individual Split Surfaces
        for srf in splitSrfs:
            theSrf = sc.doc.Objects.Find(srf)
            theSrf.Attributes.WireDensity = 0
            theSrf.CommitChanges()
        
        if delOrigSrf:
            sc.doc.Objects.Delete(srfGuid, True)
        
        sc.doc.Objects.Delete(polySrf, True)
        
        return retSrf
        
    #Get 0 to 1 T at full Curve Domain
    @staticmethod
    def paramAtRemappedDomain(t,sDom,eDom):
        return (t * (eDom - sDom)) + sDom
    
    #Trim Offset Curves
    @staticmethod
    def trimOffsetCurves(crvGuids):
        intersectParams = {}
        
        for x in range(0, crvGuids.Count):
            intersectParams[x] = []
            
        for x in range(0, crvGuids.Count - 1):
            for y in range(x + 1, crvGuids.Count):
                if crvGuids[x] != crvGuids[y]:
                    #Check Intersect Curves
                    crvA = rs.coercecurve(crvGuids[x])
                    crvB = rs.coercecurve(crvGuids[y])
                    intersections = rg.Intersect.Intersection.CurveCurve(crvA,crvB,sc.doc.ModelAbsoluteTolerance,sc.doc.ModelAbsoluteTolerance)
                    if intersections.Count > 0:
                        intersectParams[x].append(intersections[0].ParameterA)
                        intersectParams[y].append(intersections[0].ParameterB)
        
        retGuids = []
        
        for x in range(0, crvGuids.Count):
            if intersectParams[x][0] > intersectParams[x][1]:
                tA = intersectParams[x][1]
                tB = intersectParams[x][0]
            else:
                tA = intersectParams[x][0]
                tB = intersectParams[x][1]
                
            guid = rs.TrimCurve(crvGuids[x],(tA, tB))
            if guid != None:
                retGuids.append(guid)
            
        return retGuids
        
    #Generate Perp Line to Closed Curve and Extend to Boundary
    @staticmethod
    def perpLineOnCrv(crvGeo,t,bdys):
        
        rs.EnableRedraw(False)
        crvNurbs = crvGeo.ToNurbsCurve()
        
        sDom = crvGeo.Domain[0]
        eDom = crvGeo.Domain[1]
        
        rT = (t * (eDom - sDom)) + sDom
        frm = crvNurbs.PerpendicularFrameAt(rT)
        pAxis = -frm[1].XAxis
        
        pt = crvNurbs.PointAt(rT)
        pLine = rg.Line(pt,pAxis,1)
        
        theInitCrv = sc.doc.Objects.AddLine(pLine)
        extCrv = rs.ExtendCurve(theInitCrv,0,1,bdys)
        crvGeo = rs.coercecurve(extCrv)
        
        sc.doc.Objects.Delete(extCrv) #cleanup
        rs.EnableRedraw(True)
        return crvGeo