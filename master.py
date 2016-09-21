#Urban Simulator
#Main Program File
#Contributors: Ben Coorey

#Rhino Libraries
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc

#Urban Simulator Libraries
import urbansimulator as us

def main():
    
    rs.EnableRedraw(False)
    
    #makePlots()
    #makeNetwork()
    testSplitCurve()
    
    rs.EnableRedraw(True)
    
    
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

main()