"""
edge_proximity - checking whether a point is near an edge of a 2D polygon and if two
                 line segments are close.

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from quad_minmax import *
from vectors import *
from double_quadratic import *

def sign(x):
    if x>=0:
        return 1
    else:
        return -1

def near_edge(segstart,segend,s,BUFF):
    if abs(s.x-segstart.x)>2*BUFF and abs(s.x-segend.x)>2*BUFF and sign(s.x-segend.x)==sign(s.x-segstart.x):
        return False
    elif abs(s.y-segstart.y)>2*BUFF and abs(s.y-segend.y)>2*BUFF and sign(s.y-segend.y)==sign(s.y-segstart.y):
        return False
    ap = (segend-segstart).sqv()
    b = 2*((segstart-s).dot(segend-segstart))
    c = (segstart-s).sqv()
    if (segstart-s).sqv()<sq(BUFF) or (segend-s).sqv()<sq(BUFF):
        return True
    if (ap>0 and quad_min_le_D_int(ap,b,c,0,1,sq(BUFF))):
        return True
    return False

def segments_2D_close(segstart1,segend1,segstart2,segend2,BUFF):
    segStartXDiff    = segstart1.x - segstart2.x
    segStartEndXDiff = segstart1.x - segend2.x
    segStartYDiff    = segstart1.y - segstart2.y
    segStartEndYDiff = segstart1.y - segend2.y
    segEndXDiff      = segend1.x - segend2.x
    segEndStartXDiff = segend1.x - segstart2.x
    segEndYDiff      = segend1.y - segend2.y
    segEndStartYDiff = segend1.y - segstart2.y
    segXApart  = (abs(segStartXDiff)> 2*BUFF and abs(segStartEndXDiff) > 2*BUFF and
                  abs(segEndXDiff)> 2*BUFF and abs(segEndStartXDiff) > 2*BUFF and
                  sign(segStartXDiff) == sign(segStartEndXDiff) and
                  sign(segEndXDiff) == sign(segEndStartXDiff) and sign(segStartXDiff) == sign(segEndXDiff))
    segYApart  = (abs(segStartYDiff) > 2*BUFF and abs(segStartEndYDiff) > 2*BUFF and
                  abs(segEndYDiff) > 2*BUFF and abs(segEndStartYDiff) > 2*BUFF and
                      sign(segStartYDiff) == sign(segStartEndYDiff) and sign(segEndYDiff) == sign(segEndStartYDiff) and
                      sign(segStartYDiff) == sign(segEndYDiff))
    if (segXApart or segYApart): return False
    elif near_edge(segstart2,segend2,segstart1,BUFF): return True 
    elif near_edge(segstart2,segend2,segend1,BUFF): return True
    elif near_edge(segstart1,segend1,segstart2,BUFF): return True
    elif near_edge(segstart1,segend1,segend2,BUFF): return True
    elif ae((segend1-segstart1).sqv(),0) or ae((segend2-segstart2).sqv(),0): return False
    s=segstart1-segstart2
    v=segend1-segstart1
    w=segend2-segstart2
    a=v.sqv()
    b=w.sqv()
    c=-2*(v.dot(w))
    d=2*(s.dot(v))
    ee=-2*(s.dot(w))
    f=s.sqv()
    return quad_min_unit_box(a,b,c,d,ee,f,sq(BUFF))

def closest_point(segstart,segend,s,BUFFER):
    if (segend-segstart).norm()<=BUFFER: return segstart
    elif (s-segstart).dot(segend-segstart)<=0: return segstart
    elif (s-segend).dot(segstart-segend)<=0: return segend
    else:
        normdir = (segend-segstart)*(1/(segend-segstart).norm())
        tt = (segstart-s).det(normdir)
        return s+(normdir.perpR())*tt
