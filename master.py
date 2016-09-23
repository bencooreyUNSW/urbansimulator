#Urban Simulator
#Main Program File
#Contributors: Ben Coorey

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc

import math, random

import urbansimulator as us

def main():
    
    theLine = rs.GetObject("Pick Line", rs.filter.curve)
    theLineGeo = rs.coercecurve(theLine)
    
    tS = us.Boundary(theLineGeo , 1)
    tS.offsetCurve(True)
    
    #bD = us.Boundary(theLineGeo , 0)
    #rD = us.Road(theLineGeo , 0)
    
    
    #bD.offsetCurve(1)
    #rD.offsetCurve(1)
    #makePlots()
    #makeNetwork()
    #testSplitCurve()
    #testTrimOffsetCurves()
    #testCrvGenerator()
    
    rs.Redraw()
    
    
def makePlots():
    #Construct Grid
    cG = us.Grid(5,7,10,7)
    
    #Construct Plots
    cP = us.Plots(cG)
    
    #Draw Plots
    cP.drawPlots()
    
    theBld = us.Building(cP.plots[0][0].plotPolyline,1,5)
    theBld.construct()

def makeNetwork():
    thePt = rg.Point3d(0,0,0)
    theVec = rg.Vector3d(0,10,0)
    
    theNetwork = us.Network(thePt, theVec, 100, 15, 5)
    
    
def testSplitCurve():
    selSrf = rs.GetObject("Select Surface", rs.filter.surface)
    selCrvs = rs.GetObjects("Select Curves", rs.filter.curve)
    
    us.util.splitSrfwCrvs(selSrf,selCrvs,True,True)

def testTrimOffsetCurves():
    crvs = rs.GetObjects("Select Curves",rs.filter.curve)
    us.util.trimOffsetCurves(crvs)

def testCrvGenerator():
    
    crv = rs.GetObject("boundary", rs.filter.curve, True)
    bdys = []
    bdys.append(crv)
    
    tval = random.random()
    theCrv = us.util.perpLineOnCrv(crv, tval, 1,bdys)
    bdys.append(theCrv)
    tval = random.random()
    theCrv2 = us.util.perpLineOnCrv(theCrv, tval, 1,bdys)
    bdys.append(theCrv2)
    tval = random.random()
    theCrv3 = us.util.perpLineOnCrv(theCrv2, tval, 1,bdys)
    bdys.append(theCrv3)
    tval = random.random()
    theCrv4 = us.util.perpLineOnCrv(theCrv3, tval, 1,bdys)
    bdys.append(theCrv4)
    tval = random.random()
    theCrv5 = us.util.perpLineOnCrv(theCrv4, tval, 1,bdys)
    bdys.append(theCrv5)


main()