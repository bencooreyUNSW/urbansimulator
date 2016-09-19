#Network Class
#Transport Network
#Contributors: Ben Coorey

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc
import math
import random


class Network:
    #Define and initiate the class
    def __init__(self,startPt, vec, length, angle, count):
        self.startPt = startPt
        self.vec = vec
        self.length = length
        self.angle = angle
        self.cnt = count
        self.drawSegments(self.startPt, self.vec, self.length, self.angle, self.cnt)
    
    def drawSegments(self, startPt, vec, length, ang, cnt):
        if cnt > 0:
            #calculate new direction and length
            theAngle = math.radians(random.randint(-ang,ang))
            
            if cnt % 2 == 0:
                anglePerp = math.radians(70)
            else:
                anglePerp = math.radians(-70)
            
            vec.Unitize()
            newVecCont = rg.Vector3d.Multiply(length,vec)
            newVecBranch = rg.Vector3d.Multiply(length,vec)
            
            newVecCont.Rotate(theAngle,rg.Vector3d(0,0,1))
            newVecBranch.Rotate(anglePerp,rg.Vector3d(0,0,1))
            
            #construct line and add to document
            line = rg.Line(startPt,newVecCont)
            sc.doc.Objects.AddLine(line)
            
            line2 = rg.Line(line.PointAt(1),newVecBranch)
            sc.doc.Objects.AddLine(line2)
            
            theCurve = line.ToNurbsCurve()
            
            curves = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), 3, sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
            curves2 = theCurve.Offset(rg.Plane(rg.Point3d(0,0,0),rg.Vector3d(0,0,1)), -3, sc.doc.ModelAbsoluteTolerance, rg.CurveOffsetCornerStyle.None)
            
            for offset_curve in curves:
                sc.doc.Objects.AddCurve(offset_curve)
            for offset_curve in curves2:
                sc.doc.Objects.AddCurve(offset_curve)
            
            #increment segment count
            cnt -= 1
            
            #draw next segment
            self.drawSegments(line.PointAt(1), newVecCont, length * .95, ang, cnt)
            self.drawSegments(line2.PointAt(1), newVecBranch, length * .7, ang, cnt - 1 )
