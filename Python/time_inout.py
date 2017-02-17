"""
time_inout - computing times to enter-exit a 2D polygon region by a point (moving)

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from edge_proximity import *
from polygon_contain import *
from moving_polygon import *
from double_quadratic import *
import detection

def dot_zero_linear_2D_alg(B,T,w,v,a,b,eps):
  aa = v.dot(b)
  bb = w.dot(b) + a.dot(v)
  cc = w.dot(a)
  if not ae(aa,0) and discr(aa,bb,cc)>=0:
    return root(aa,bb,cc,eps)
  if not ae(bb,0):
    return -cc/bb
  if eps==-1:
    return B
  return T

def lookahead_proj(B,T,t):
  if t>T: return T
  if t<B: return B
  return t

def swap_times(B,T,s,v,segstart,segend,startvel,endvel):
  t0=dot_zero_linear_2D_alg(B,T,s-segstart,v-startvel,
                            (segend-segstart).perpR(),(endvel-startvel).perpR(),-1)
  t1=dot_zero_linear_2D_alg(B,T,s-segstart,v-startvel,
	   (segend-segstart).perpR(),(endvel-startvel).perpR(),1)
  t2=dot_zero_linear_2D_alg(B,T,s-segstart,v-startvel,segend-segstart,endvel-startvel,1)
  t3=dot_zero_linear_2D_alg(B,T,s-segstart,v-startvel,segend-segstart,endvel-startvel,-1)
  t4=dot_zero_linear_2D_alg(B,T,s-segend,v-endvel,segstart-segend,startvel-endvel,-1)
  t5=dot_zero_linear_2D_alg(B,T,s-segend,v-endvel,segstart-segend,startvel-endvel,1)
  return [ lookahead_proj(B,T,t0),lookahead_proj(B,T,t1),lookahead_proj(B,T,t2),
           lookahead_proj(B,T,t3),lookahead_proj(B,T,t4),lookahead_proj(B,T,t5) ]

def all_times(B,T,mp,s,v,Fac):
  lastout=False
  times = [B,T]
  for i in range(len(mp.polystart)):
      nexti = (i+1 if i<len(mp.polystart)-1 else 0)
      if (not detection.edge_detect(T-B,s+v*B,v,mp.polystart[i]+mp.polyvel[i]*B,
                          mp.polystart[nexti]+mp.polyvel[nexti]*B,mp.polyvel[i],mp.polyvel[nexti],Fac)):
        continue
      thistime = swap_times(B,T,s,v,mp.polystart[i],mp.polystart[nexti],
                            mp.polyvel[i],mp.polyvel[nexti])
      times=times+thistime
  print("\n\n number of edges crossed is "+str(int(len(times)/6))+" \n\n")
  unique = []
  [unique.append(t) for t in times if t not in unique]
  unique.sort()
  return unique

def times_in_out(B,T,mp,s,v,BUFF,Fac):
  lastin=False
  ans = []
  at = all_times(B,T,mp,s,v,Fac)
  for i in range(0,len(at)-1):
    t1=at[i]
    t2=at[i+1]
    midpt = (t1+t2)/2.000
    polyat = mp.at(midpt)
    inside = (not definitely_outside(polyat,s+(v*midpt),BUFF))
    if inside and (not lastin):
      ans.append([t1,t2])
      lastin=True
    elif inside:
      last=ans[len(ans)-1]
      ans.pop(len(ans)-1)
      new=[last[0],t2]
      ans.append(new)
      lastin=True
    else:
      lastin=False
  print("\n\n time in out answer is "+str(ans)+"\n\n")
  return ans

def time_detector(B,T,mp,s,v,BUFF,Fac):
  tio = times_in_out(B,T,mp,s,v,BUFF,Fac)
  return (len(tio)>0)
    

# mypoly = [Vector(0,-5),Vector(2,2),Vector(0,0),Vector(-2,2)]

# myvel = [Vector(-1,0),Vector(-1,0),Vector(-1,0),Vector(-1,0)]

# mp = MovingPolygon(mypoly,myvel)

# a = times_in_out(0,10,mp,Vector(-5,1),Vector(1,0),0.00001)

# print("And answer is is "+str(a))




