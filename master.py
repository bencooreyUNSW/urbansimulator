#Urban Simulator
#Main Program File
#Contributors: Ben Coorey

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc

import math, random

import urbansimulator as us

def main():
    
    siteSrf = rs.GetObject("Select Precinct Boundary", rs.filter.surface)
    typedSite = us.typedSurface(siteSrf)
    project = us.Precinct(typedSite)
    
    rs.Redraw()

main()