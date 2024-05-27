from __future__ import print_function
import numpy as np

def CheckTriWinding(tri, allowReversed):
    trisq = np.ones((3,3))
    trisq[:,0:2] = np.array(tri)
    detTri = np.linalg.det(trisq)
    if detTri < 0.0:
        if allowReversed:
            a = trisq[2,:].copy()
            trisq[2,:] = trisq[1,:]
            trisq[1,:] = a
        else: raise ValueError("triangle has wrong winding direction")
    return trisq

def TriTri2D(t1, t2, eps = 0.0, allowReversed = False, onBoundary = True):

    t1s = CheckTriWinding(t1, allowReversed)
    t2s = CheckTriWinding(t2, allowReversed)

    if onBoundary:

        chkEdge = lambda x: np.linalg.det(x) < eps
    else:

        chkEdge = lambda x: np.linalg.det(x) <= eps


    for i in range(3):
        edge = np.roll(t1s, i, axis=0)[:2,:]

        if (chkEdge(np.vstack((edge, t2s[0]))) and
            chkEdge(np.vstack((edge, t2s[1]))) and  
            chkEdge(np.vstack((edge, t2s[2])))):
            return False


    for i in range(3):
        edge = np.roll(t2s, i, axis=0)[:2,:]

        if (chkEdge(np.vstack((edge, t1s[0]))) and
            chkEdge(np.vstack((edge, t1s[1]))) and  
            chkEdge(np.vstack((edge, t1s[2])))):
            return False


    return True

if __name__=="__main__":
    t1 = [[0,0],[5,0],[0,5]]
    t2 = [[0,0],[5,0],[0,6]]
    print (TriTri2D(t1, t2), True)

    t1 = [[0,0],[0,5],[5,0]]
    t2 = [[0,0],[0,6],[5,0]]
    print (TriTri2D(t1, t2, allowReversed = True), True)

    t1 = [[0,0],[5,0],[0,5]]
    t2 = [[-10,0],[-5,0],[-1,6]]
    print (TriTri2D(t1, t2), False)

    t1 = [[0,0],[5,0],[2.5,5]]
    t2 = [[0,4],[2.5,-1],[5,4]]
    print (TriTri2D(t1, t2), True)

    t1 = [[0,0],[1,1],[0,2]]
    t2 = [[2,1],[3,0],[3,2]]
    print (TriTri2D(t1, t2), False)

    t1 = [[0,0],[1,1],[0,2]]
    t2 = [[2,1],[3,-2],[3,4]]
    print (TriTri2D(t1, t2), False)


    t1 = [[0,0],[1,0],[0,1]]
    t2 = [[1,0],[2,0],[1,1]]
    print (TriTri2D(t1, t2, onBoundary = True), True)

    t1 = [[0,0],[1,0],[0,1]]
    t2 = [[1,0],[2,0],[1,1]]
    print (TriTri2D(t1, t2, onBoundary = False), False)
