#Urban Simulator
#Main Program File
#Contributors: Ben Coorey

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc

import math, random

import urbansimulator as us

def main():
    
    #rs.EnableRedraw(False)
    
    siteSrf = rs.GetObject("Select Precinct Boundary", rs.filter.surface)
    typedSite = us.typedSurface(siteSrf)
    
    project = us.Precinct(typedSite,4)
    
    project.roadNetwork.draw()
    
    #rs.EnableRedraw(True)
    
    rs.Redraw()

main()