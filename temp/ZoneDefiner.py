import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

zone=[]
listofareas=[]
listofpoints=[]
distances=[]
myBlocks= rs.GetObjects("select srfs",8)

point1= rs.GetPoint("get point")

#blockArea =rs.Area(myBlocks)

for i in myBlocks:
    area = rs.Area(i)
    listofareas.append(area)




for i in myBlocks:
    test= rs.coercesurface(i)
    amp = rg.AreaMassProperties.Compute(test)
    areaPt = amp.Centroid
    listofpoints.append(area)



coercedpoints = rs.coerce3dpointlist(listofpoints)

for i in coercedpoints:
    rs.AddLine(point1,i)
    
print distances


"""
print listofpoints
for i in listofpoints:
    rs.AddPoint(i)
 v
for i in listofareas:
    if i < 20000:
        zonetemp = 1
    else:
    
    
   """
