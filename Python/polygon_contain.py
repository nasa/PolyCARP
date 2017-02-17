"""
polygon_contain - containment for 2D polygons

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from acceptable_polygon import *
from copy import deepcopy

def near_any_edge(p,s,BUFF):
    for i in range(len(p)):
        if near_poly_edge(p,s,BUFF,i):
            return True
    return False

class NumEdgesCross:
    
    def __init__(self, num = True, invalid = True):
        self.num = num
        self.invalid = invalid
        
    def __str__(self):
        return "( num:=" + str(self.num) + ", invalid:=" + str(self.invalid) + " )"

def number_upshot_crosses(p,s):
    num = 0
    invalid = False
    for i in range(len(p)):
        uce = upshot_crosses_edge(p,s,i)
        if uce.ans: num=num+1
        if uce.invalid: invalid = True
    return NumEdgesCross(num,invalid)

def quadrant(s):
    if s.x>=0 and s.y>=0: return 1
    if s.x<=0 and s.y>=0: return 2
    if s.x<=0: return 3
    return 4

def winding_number(p,s):
    #print("calling winding_number with p = "+str(p))
    total = 0
    q = quadrant(p[0]-s)
    for i in range(len(p)):
        k = q
        thisv = p[i]-s
        nextv = (p[i+1]-s if i<len(p)-1 else p[0]-s)
        q = quadrant(nextv)
        if k==q: continue
        elif q-1==(k % 4):
            total = total+1
        elif k-1==(q % 4):
            total = total-1
        elif (nextv-thisv).det(thisv)<=0: total=total+2
        else: total=total-2
    return int(total/4)

def fix_polygon(p,s,BUFF):
    newp = deepcopy(p)
    for i in range(len(p)):
        if p[i].y>=s.y-BUFF and abs(p[i].x-s.x)<BUFF:
            newp[i]=p[i]-Vector(2*BUFF,0)
    return newp

def definitely_inside_prelim(p,s,BUFF):
    mcdi = min_cross_dist_index(p,s)
    nuc = number_upshot_crosses(p,s)
    if mcdi.index<0:
        return False
    if nuc.invalid:
        return False
    if p[mcdi.index].x<s.x:
        return False
    next_ind = (mcdi.index+1 if mcdi.index<len(p)-1 else 0)
    if p[next_ind].x>s.x:
        return False
    if (nuc.num % 2)==0:
        return False
    if near_any_edge(p,s,BUFF):
        return False
    return True

def definitely_inside(p,s,BUFF):
    fixp = fix_polygon(p,s,BUFF)
    insidefixp = definitely_inside_prelim(fixp,s,BUFF)
    if near_any_edge(p,s,BUFF):
        return False
    if near_any_edge(fixp,s,BUFF):
        return False
    if not insidefixp:
        return False
    if winding_number(p,s)!=1:
        return False
    return True

def definitely_outside_prelim(p,s,BUFF):
    # print("calling dop with s = "+str(s)+" and BUFF = "+str(BUFF))
    mcdi = min_cross_dist_index(p,s)
    nuc = number_upshot_crosses(p,s)
    if near_any_edge(p,s,BUFF):
        # print("was near an edge")
        return False
    if nuc.invalid:
        # print("was invalid")
        return False
    if mcdi.index<0:
        # print("no crosses")
        return True
    if p[mcdi.index].x>s.x:
        # print("crosses answer")
        return False
    next_ind = (mcdi.index+1 if mcdi.index<len(p)-1 else 0)
    if p[next_ind].x<s.x: return False
    if (nuc.num % 2)!=0: return False
    return True

def definitely_outside(p,s,BUFF):
    fixp = fix_polygon(p,s,BUFF)
    outsidefixp = definitely_outside_prelim(fixp,s,BUFF)
    if near_any_edge(p,s,BUFF): return False
    if near_any_edge(fixp,s,BUFF): return False
    if not outsidefixp: return False
    if winding_number(p,s)!=0: return False
    return True

def nice_polygon_2D(p,BUFF):
    accept = acceptable_polygon_2D(p,BUFF)
    # counterc = counterclockwise_edges(p)
    defout = definitely_outside(p,test_point_below(p,BUFF),BUFF)
    return (accept and defout)
