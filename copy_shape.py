#Copy Shape
import maya.cmds as cmds

def copyShape(src,dst):#source,destination
    vtxCount = cmds.polyEvaluate(src, v=True)#getting total number of vertices in a polygon
    print(vtxCount)#= 42
    for i in range(vtxCount):
        vtxID = f'{src}.vtx[{i}]'#src.vtx0, src.vtx1, src.vtx2, ...
        srcVtxPos = cmds.xform(vtxID, q=True,t=True,os=True)
        
        dstVtxID = f'{dst}.vtx[{i}]'
        cmds.xform(dstVtxID,t=srcVtxPos,os=True)#change position of destination vertex to match the source vertex
    
copyShape('pCylinder2','pCylinder1')