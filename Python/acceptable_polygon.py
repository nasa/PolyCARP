"""
acceptable_polygon - determining if a 2D polygon is well-formed

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""


from edge_proximity import *
from convex_polygon_containment import *

def near_poly_edge(p,s,BUFF,i):
    next_ind = (i+1 if i<len(p)-1 else 0)
    return near_edge(p[i],p[next_ind],s,BUFF)

def printpoly(p):
    ans = "["
    for i in range(len(p)):
        ans = ans+str(p[i])+","
    ans = ans + "]"
    return ans

class EdgeCross:
    
    def __init__(self, ans = True, invalid = True):
        self.ans = ans
        self.invalid = invalid
        
    def __str__(self):
        return "( ans:=" + str(self.ans) + ", invalid:=" + str(self.invalid) + " )"

def upshot_crosses_edge(p,s,i):
    next_ind = (i+1 if i<len(p)-1 else 0)
    tester = (p[next_ind].x-p[i].x)**2*(p[i].y-s.y) + (s.x-p[i].x)*(p[next_ind].y-p[i].y)*(p[next_ind].x-p[i].x)
    if p[i].x>s.x and p[next_ind].x>s.x: return EdgeCross(False,False)
    elif p[i].x<s.x and p[next_ind].x<s.x: return EdgeCross(False,False)
    elif ae(p[i].x,p[next_ind].x) and (p[i].y>=s.y or p[next_ind].y>=s.y): return EdgeCross(True,True)
    elif ae(p[i].x,p[next_ind].x): return EdgeCross(False,False)
    elif tester>=0: return EdgeCross(True,False)
    return EdgeCross(False,False)


class CrossAns:
    
    def __init__(self, index = 0, num = 0, denom = 1):
        self.index = index
        self.num = num
        self.denom = denom
        
    def __str__(self):
        return "( index:="+str(self.index)+", num:="+str(self.num)+", denom:="+str(self.denom)+" )"

def compute_intercept(p,s,i):
    next_ind = (i+1 if i<len(p)-1 else 0)
    if ((p[i].x>s.x and p[next_ind].x>s.x) or
       (p[i].x<s.x and p[next_ind].x<s.x) or
       ae(p[i].x,p[next_ind].x)):
        return CrossAns(-1,1,1)
    newnum = (p[i].y-s.y)*(p[next_ind].x-p[i].x) + \
	  	    (s.x-p[i].x)*(p[next_ind].y-p[i].y)
    newdenom = p[next_ind].x-p[i].x
    if newnum*newdenom<0: ans = CrossAns(-1,1,1)
    else: ans = CrossAns(i,newnum,newdenom)
    # print("for edge "+str(i)+" returning ans "+str(ans))
    return ans


def min_cross_dist_index(p,s):
    curr = compute_intercept(p,s,0)
    for j in range(1,len(p)):
        cii = compute_intercept(p,s,j)
        if curr.index<0:
            curr = cii
            continue
        if cii.index<0:
            continue
        if curr.denom**2*cii.num*cii.denom<curr.num*curr.denom*cii.denom**2:
            curr = cii
    # print("curr answer is "+str(curr))
    return curr

def corner_lt_3deg(v,w):
    if v.norm()<=0.1 or w.norm()<=0.1:
        return True
    if v.dot(w)<-0.9986295347545738*(v.norm()*w.norm()): #(cosine of angle)
        return True
    return False

    

def acceptable_polygon_2D(p,BUFF):
    if len(p)<=2:
        return False
    for i in range(len(p)):
        for j in range(i,len(p)):
            mi = (i+1 if i<len(p)-1 else 0)
            mj = (j+1 if j<len(p)-1 else 0)
            pj = p[j]
            pi = p[i]
            pmi = p[mi]
            pmj = p[mj]
            if i==j: continue
            if pi.ae(pj):
                return False
            if j==mi and (near_poly_edge(p,pmj,BUFF,i) or
                          near_poly_edge(p,pi,BUFF,j)):
                return False
            if j==mi and corner_lt_3deg(pj-pi,pmj-pj):
                return False
            if j==mi: continue
            if i==mj and (near_poly_edge(p,pmi,BUFF,j) or
                          near_poly_edge(p,pj,BUFF,i)):
                return False
            if i==mj and corner_lt_3deg(pi-pj,pmi-pi):
                return False
            if i==mj: continue
            if segments_2D_close(pi,pmi,pj,pmj,BUFF):
                return False
    return True

def counterclockwise_corner_index(p,eps):
    windex = 0
    for i in range(1,len(p)):
        if ae(p[windex].x,p[i].x) and p[windex].y>=p[i].y:
            windex = i
        if ae(p[windex].x,p[i].x): continue
        if eps*p[windex].x>eps*p[i].x:
            windex = i
    return windex

def min_y_val(p):
    curr = p[0].y
    for i in range(1,len(p)):
        if p[i].y<=curr:
            curr = p[i].y
    return curr

def test_point_below(p,BUFF):
    minxindex = counterclockwise_corner_index(p,1)
    maxxindex = counterclockwise_corner_index(p,-1)
    minx = p[minxindex].x
    maxx = p[maxxindex].x
    return Vector((minx+maxx)/2,min_y_val(p)-abs(maxx-minx)-2*BUFF)

def counterclockwise_edges(p):
    l = counterclockwise_corner_index(p,1)
    r = counterclockwise_corner_index(p,-1)
    lprev = (l-1 if l>0 else len(p)-1)
    rprev = (r-1 if r>0 else len(p)-1)
    lnext_ind = (l+1 if l<len(p)-1 else 0)
    rnext_ind = (r+1 if r<len(p)-1 else 0)
    LPP = p[l]-p[lprev]
    LPN = p[lnext_ind]-p[l]
    RPP = p[r]-p[rprev]
    RPN = p[rnext_ind]-p[r]
    Lcc = (LPP.det(LPN)>0)
    Rcc = (RPP.det(RPN)>0)
    return Lcc and Rcc

def segment_near_any_edge(p,BUFF,segstart,segend):
    for i in range(len(p)):
        mi = (i+1 if i<len(p)-1 else 0)
        if segments_2D_close(segstart,segend,p[i],p[nexti],BUFF):
            return True
    return False
