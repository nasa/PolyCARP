"""
detection - collision detection between a point and a 2D polygon

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from polygon_contain import *
from moving_polygon import *
from double_quadratic import *

def dot_nneg_linear_2D_alg(T,w,v,a,b,eps):
    aa = v.dot(b)
    bb = w.dot(b)+a.dot(v)
    cc = w.dot(a)
    if not ae(aa,0):
        if discr(aa,bb,cc)>=0:
            if aa<0: [intl,intu]=[root(aa,bb,cc,1),root(aa,bb,cc,-1)]
            elif eps==-1: [intl,intu]=[0,root(aa,bb,cc,-1)]
            else: [intl,intu]=[root(aa,bb,cc,1),T]
        elif aa>0: [intl,intu]=[0,T]
        else: [intl,intu]=[T,0]
    elif ae(bb,0) and cc>=0: [intl,intu]=[0,T]
    elif ae(bb,0): [intl,intu]=[T,0]
    elif bb>0: [intl,intu]=[-cc/bb,T]
    else: [intl,intu]=[0,-cc/bb]
    if (intu<intl or intu<0 or intl>T):
        return [T,0]
    else: return [max(intl,0),min(intu,T)]

def dot_nneg_spec(T,w,v,a,b,eps,eps2,Fac):
    ww = a.Scal(Fac)+w.Scal(eps2)
    vv = b.Scal(Fac)+v.Scal(eps2)
    return dot_nneg_linear_2D_alg(T,ww,vv,a,b,eps)




def edge_detect_simple(T,w,v,a,b,Fac): # Fac close to 0
    [Vlbn,Vubn] = dot_nneg_spec(T,w,v,a,b,-1,-1,1+Fac)
    [Vlb,Vub] = dot_nneg_spec(T,w,v,a,b,-1,1,1+Fac)
    [Vlbnx,Vubnx] = dot_nneg_spec(T,w,v,a,b,1,-1,1+Fac)
    [Vlbx,Vubx] = dot_nneg_spec(T,w,v,a,b,1,1,1+Fac)
    [Plbn,Pubn] = dot_nneg_spec(T,w,v,a.perpR(),b.perpR(),-1,-1,Fac)
    [Plb,Pub] = dot_nneg_spec(T,w,v,a.perpR(),b.perpR(),-1,1,Fac)
    [Plbnx,Pubnx] = dot_nneg_spec(T,w,v,a.perpR(),b.perpR(),1,-1,Fac)
    [Plbx,Pubx] = dot_nneg_spec(T,w,v,a.perpR(),b.perpR(),1,1,Fac)
    Vlb1 = max(Vlb,Vlbn)
    Vub1 = min(Vub,Vubn)
    Vlb2 = max(Vlb,Vlbnx)
    Vub2 = min(Vub,Vubnx)
    Vlb3 = max(Vlbx,Vlbn)
    Vub3 = min(Vubx,Vubn)
    Vlb4 = max(Vlbx,Vlbnx)
    Vub4 = min(Vubx,Vubnx)
    Plb1 = max(Plb,Plbn)
    Pub1 = min(Pub,Pubn)
    Plb2 = max(Plb,Plbnx)
    Pub2 = min(Pub,Pubnx)
    Plb3 = max(Plbx,Plbn)
    Pub3 = min(Pubx,Pubn)
    Plb4 = max(Plbx,Plbnx)
    Pub4 = min(Pubx,Pubnx)
    if max(Vlb1,Plb1)<=min(Vub1,Pub1): return True
    if max(Vlb1,Plb2)<=min(Vub1,Pub2): return True
    if max(Vlb1,Plb3)<=min(Vub1,Pub3): return True
    if max(Vlb1,Plb4)<=min(Vub1,Pub4): return True
    if max(Vlb2,Plb1)<=min(Vub2,Pub1): return True
    if max(Vlb2,Plb2)<=min(Vub2,Pub2): return True
    if max(Vlb2,Plb3)<=min(Vub2,Pub3): return True
    if max(Vlb2,Plb4)<=min(Vub2,Pub4): return True
    if max(Vlb3,Plb1)<=min(Vub3,Pub1): return True
    if max(Vlb3,Plb2)<=min(Vub3,Pub2): return True
    if max(Vlb3,Plb3)<=min(Vub3,Pub3): return True
    if max(Vlb3,Plb4)<=min(Vub3,Pub4): return True
    if max(Vlb4,Plb1)<=min(Vub4,Pub1): return True
    if max(Vlb4,Plb2)<=min(Vub4,Pub2): return True
    if max(Vlb4,Plb3)<=min(Vub4,Pub3): return True
    if max(Vlb4,Plb4)<=min(Vub4,Pub4): return True
    return False

def edge_detect(T,s,v,segstart,segend,startvel,endvel,Fac):
    midpt = (segend+segstart).Scal(0.5)
    news  = s-midpt
    midv  =(endvel+startvel).Scal(0.5)
    return edge_detect_simple(T,s-midpt,v-midv,segend.Scal(0.5)-
                       segstart.Scal(0.5),endvel.Scal(0.5)-startvel.Scal(0.5),Fac)

def Collision_Detector(T,mp,s,v,BUFF,Fac):
    if not definitely_outside(mp.polystart,s,BUFF):
        return True
    for i in range(len(mp.polystart)):
        nexti = (i+1 if i<len(mp.polystart)-1 else 0)
        if edge_detect(T,s,v,mp.polystart[i],mp.polystart[nexti],
                       mp.polyvel[i],mp.polyvel[nexti],Fac):
            return True
    return False

def Static_Collision_Detector(B,T,p,s,v,BUFF):
    if not definitely_outside(p,s+v*B,BUFF):
        return True
    if not definitely_outside(p,s+v*T,BUFF):
        return True
    for i in range(len(p)):
        nexti = (i+1 if i<len(p)-1 else 0)
        if segments_2D_close(p[i],p[nexti],s+v*B,s+v*T,BUFF):
            return True
    return False


