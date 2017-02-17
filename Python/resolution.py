"""
resolution - algorithms to compute a point to resolve to if a point needs to get outside
             or inside a polygon region.

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from polygon_contain import *

def proj_vect(u,v,w,BUFF):
    if (v-u).norm()<=BUFF or (w-v).norm()<=BUFF:
        return Vector(1,1)
    elif (v-u).dot(w-v)>=0:
        return (v-u).perpR().hat()+(w-v).perpR().hat()
    elif (w-v).det(v-u)<=0:
        return (v-u).hat()+(v-w).hat()
    else:
        return (u-v).hat()+(w-v).hat()

def modifiable_to_size(p,BUFF,ResolBUFF):
    return (nice_polygon_2D(p,BUFF) and acceptable_polygon_2D(p,2*ResolBUFF+BUFF))

def expand_polygon_2D(p,BUFF,ResolBUFF):
    ans=[]
    for i in range(len(p)):
        prevv = p[i-1] if i>0 else p[len(p)-1]
        nextv = p[i+1] if i<len(p)-1 else p[0]
        pv = proj_vect(prevv,p[i],nextv,BUFF)
        R = (p[i]-prevv).perpR().hat()
        q = p[i]+R.Scal(ResolBUFF)
        tt = (0 if abs(pv.dot(R))<=(BUFF/100.00) else ((q-p[i]).dot(R))/(pv.dot(R)))
        ans.append(p[i]+pv.Scal(tt))
    return ans

def contract_polygon_2D(p,BUFF,ResolBUFF):
    ans=[]
    for i in range(len(p)):
        prevv = p[i-1] if i>0 else p[len(p)-1]
        nextv = p[i+1] if i<len(p)-1 else p[0]
        pv = proj_vect(prevv,p[i],nextv,BUFF)
        R = (p[i]-prevv).perpR().hat()
        q = p[i]-R.Scal(ResolBUFF)
        tt = (0 if abs(pv.dot(R))<=(BUFF/100.00) else ((q-p[i]).dot(R))/(pv.dot(R)))
        ans.append(p[i]+pv.Scal(tt))
    return ans

def closest_edge(p,BUFF,s):
    ce=0
    for i in range(1,len(p)):
        next = i+1 if i<len(p)-1 else 0
        closp = closest_point(p[i],p[next],s,BUFF)
        thisdist = (s-closp).norm()
        nextce = ce+1 if ce<len(p)-1 else 0
        prevclosp = closest_point(p[ce],p[nextce],s,BUFF)
        prevdist = (s-prevclosp).norm()
        if thisdist<prevdist: ce=i
    return ce

def recovery_test_point(BUFF,ResolBUFF,p,s,eps):
    i = closest_edge(p,BUFF,s)
    nexti = i+1 if i<len(p)-1 else 0
    ip = closest_point(p[i],p[nexti],s,BUFF)
    dirvect = (p[nexti]-p[i]).perpR()
    testdir = (dirvect).hat()
    testvect = ip+testdir.Scal(eps*(ResolBUFF+BUFF/2))
    return testvect

def recovery_point(BUFF,ResolBUFF,p,s,eps):
    if eps==1 and definitely_outside(p,s,BUFF) and (not near_any_edge(p,s,ResolBUFF)):
        return s
    if eps==-1 and definitely_inside(p,s,BUFF) and (not near_any_edge(p,s,ResolBUFF)):
        return s
    tv = recovery_test_point(BUFF,ResolBUFF,p,s,eps)
    if eps==1 and definitely_outside(p,tv,BUFF) and (not near_any_edge(p,tv,ResolBUFF)):
        return tv
    if eps==-1 and definitely_inside(p,tv,BUFF) and (not near_any_edge(p,tv,ResolBUFF)):
        return tv
    i = closest_edge(p,BUFF,s)
    nexti = i+1 if i<len(p)-1 else 0
    neari = i if (s-p[i]).sqv()<=(s-p[nexti]).sqv() else nexti
    nearnexti = neari+1 if neari<len(p)-1 else 0
    nearprevi = neari-1 if neari>0 else len(p)-1
    V1 = p[neari]-p[nearprevi]
    V2 = p[nearnexti]-p[neari]
    leftturn = V2.det(V1)<=0
    pv = proj_vect(p[nearprevi],p[neari],p[nearnexti],BUFF)
    pvnormed = pv.hat()
    R = (p[neari]-p[nearprevi]).perpR().hat()
    q = p[neari]+R.Scal(eps*ResolBUFF)
    tt = (0 if abs(pv.dot(R))<=(BUFF/100) else ((q-p[i]).dot(R))/(pv.dot(R)))
    ans = p[neari]+pv.Scal(tt)
    if (eps==1 and leftturn) or (eps==-1 and not leftturn):
        ans = p[neari]+pvnormed.Scal(eps*ResolBUFF)
    if eps==1 and definitely_outside(p,ans,BUFF):
        return ans
    elif eps==-1 and definitely_inside(p,ans,BUFF):
        return ans
    else:
        return s

def outside_recovery_point(BUFF,ResolBUFF,p,s):
    return recovery_point(BUFF,ResolBUFF,p,s,1)

def inside_recovery_point(BUFF,ResolBUFF,p,s):
    return recovery_point(BUFF,ResolBUFF,p,s,-1)
