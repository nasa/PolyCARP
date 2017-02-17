"""
polygon_containment_test - testing containment for 2D polygons

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from polygon_contain import *
import random

iggy = 0.001

MyPoly = [Vector(0+iggy,0+iggy),Vector(1+iggy,-1+iggy),
	  Vector(1+iggy,0+iggy),Vector(2+iggy,1+iggy),
	  Vector(1+iggy,1+iggy),Vector(0+iggy,2+iggy),
	  Vector(0+iggy,1+iggy),Vector(-1+iggy,2+iggy),
	  Vector(-1+iggy,-1+iggy),Vector(0+iggy,0)]

def inmypoly(s):
    return (0<=s.x and s.x<=1 and s.y>=-s.x and s.y<=2-
            s.x) or (1<=s.x and s.x<=2 and s.y>=s.x-1 and s.y
                     <=1) or (-1<=s.x and s.x<=0 and s.y>=s.x
                              and s.y<=-s.x+1)

XNum = 100
YNum = 100
epsil = 1/10

MyBuff = 0.01

DGC = Vector(iggy,iggy)

def xtest(i):
	return -2+4*random.random()
#-2+epsil+i*(4/XNum)

def ytest(i):
	return -2+4*random.random()
#-2+epsil+i*(4/YNum)

foundprob=False

s = Vector(0,0)

for i in range(XNum):
    tbi = (i % 10 == 0)
    if tbi: print(str(i)+" and s is "+str(s))
    if foundprob: break
    for j in range(YNum):
        s = Vector(xtest(i),ytest(j))
        if definitely_inside(MyPoly,s,0.0001) \
            and (not inmypoly(s-DGC)): foundprob = True
        if definitely_outside(MyPoly,s,0.0001) \
            and inmypoly(s-DGC): foundprob = True


print("foundprob is "+str(foundprob))
