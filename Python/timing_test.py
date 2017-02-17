"""
timing_test - testing how fast are the polygon algorithms

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from detection import *
import random
import time

def poly_at_vel(pstart,vv,t):
    ans = []
    for i in range(len(pstart)):
        ans.append(pstart[i]+vv[i].Scal(t))
    return ans

def Collision_Detector_It(T,mp,s,v,BUFF,Fac):
    if not definitely_outside_prelim(mp.polystart,s,BUFF):
        return True
    for t in range(T):
        pav = poly_at_vel(mp.polystart,mp.polyvel,t)
        if not definitely_outside_prelim(pav,s+v.Scal(t),BUFF):
            return True
    return False

TT = 300

iggy = 0.001

MyPoly = [Vector(0+iggy,0+iggy),Vector(1+iggy,-1+iggy),
          Vector(1+iggy,0+iggy),Vector(2+iggy,1+iggy),
          Vector(1+iggy,1+iggy),Vector(0+iggy,2+iggy),
          Vector(0+iggy,1+iggy),Vector(-1+iggy,2+iggy),
          Vector(-1+iggy,-1+iggy),Vector(0+iggy,0)]

def gen_point():
    side = (random.randrange(0,2)>0)
    xystart = -3.0 + 6.0*random.randrange(0,2)
    xy = -3.0+6.0*random.random()
    if side: return Vector(xystart,xy)
    return Vector(xy,xystart)
    

def gen_poly():
    start = gen_point()
    end = gen_point()
    basevel = (end-start).Scal(1.00/(1.00*TT))
    genvel = []
    for i in range(len(MyPoly)):
        thisvel = basevel + gen_point().Scal(1.00/(12.00*TT))
        genvel.append(thisvel)
    return MovingPolygon(MyPoly,genvel)

trues = 0
falses = 0

start_time = time.time()

for i in range(100):
    if (i % 10)==0: print(str(i))
    start = gen_point()
    end = gen_point()
    genvel = (end-start).Scal(1.00/(1.00*TT))
    ans = Collision_Detector(TT,gen_poly(),gen_point(),genvel,0.001,0.001)
    if ans: trues = trues+1
    else: falses = falses+1


print("Analytic took --- %s seconds ---" % (time.time() - start_time))
print(str(trues)+" are true and "+str(falses)+" are false")


trues = 0
falses = 0

start_time = time.time()

for i in range(100):
    if (i % 10)==0: print(str(i))
    start = gen_point()
    end = gen_point()
    genvel = (end-start).Scal(1.00/(1.00*TT))
    ans = Collision_Detector_It(TT,gen_poly(),gen_point(),genvel,0.001,0.001)
    if ans: trues = trues+1
    else: falses = falses+1


print("Iterative took --- %s seconds ---" % (time.time() - start_time))
print(str(trues)+" are true and "+str(falses)+" are false")
