"""
convex_polygon_containment - containment for 2D convex polygons

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

import vectors

def on_left_of_edge(p,i,j):
    next_ind = (i+1 if i<len(p)-1 else 0)
    return ((p[next_ind]-p[i]).det(p[j]-p[i])>=0)

def counterclockwise_convex(p):
    for i in range(len(p)):
        for j in range(len(p)):
            if j!=i and j!=(i+1 if i<len(p)-1 else 0) and not on_left_of_edge(p,i,j):
                return False
    return True
    
def left_of_segment_2D(p,j,s):
    next_ind = (j+1 if j<len(p)-1 else 0)
    return ((p[next_ind]-p[j]).det(s-p[j])>=0)

def inside_convex_2D(p,s):
    for i in range(0,len(p)):
        if not left_of_segment_2D(p,i,s):
            return False
    return True

def inside_some_convex_2D(plist,s):
    for i in range(0,len(plist)):
        if inside_convex_2D(plist[i],s): return True
    return False
