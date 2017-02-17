"""
inouttest - testing whether the containment functions perform as expected on an example

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from polygon_contain import *
import random
import time

BUFF = 0.0000000000001

UseNum=True
UseMCDI=False
UseWinding=False

# BUFF = 0.0000000000001

# fixp = [Vector(-4.7200000000002,4.426666666666668),
#         Vector(-0.2400000000000002,2.666666666666666),
#         Vector(-2.2666666666666666,6.906666666666666),
#         Vector(-7.466666666666667,7.173333333333332),
#         Vector(-8.373333333333333,3.040000000000001),
#         Vector(-8.186666666666667,-0.8800000000000008),
#         Vector(-4.64,-2.826666666666666),
#         Vector(1.626666666666667,1.173333333333332),
#         Vector(2.08,2.1066666666666656),
#         Vector(1.8933333333333344,2.746666666666666),
#         Vector(0.8800000000000008,2.1866666666666656)]

# v = Vector(-4.72,-1.1994247486071519)

# print("fixp is "+printpoly(fixp))

# defin = definitely_inside_prelim(fixp,v,BUFF)

# defout = definitely_outside_prelim(fixp,v,BUFF)

# print("defin is "+str(defin))

# print("defout is "+str(defout))

# BUFF = 0.0000000000001

p = [Vector(-1,-1),
        Vector(1,-1),
        Vector(1,1),
        Vector(-1,1)]

# v = Vector(0,0)

# print("fixp is "+printpoly(fixp))

# defin = definitely_inside(fixp,v,BUFF,False,False,True)

# defout = definitely_outside(fixp,v,BUFF,False,False,True)

# print("defin is "+str(defin))

# print("defout is "+str(defout))

ins=0
outs=0
neither=0


start_time = time.time()



for i in range(40000):
  xval=-2+random.random()*4
  yval=-2+random.random()*4
  rvct = Vector(xval,yval)
  defin = definitely_inside(p,rvct,BUFF,UseNum,UseMCDI,UseWinding)
  defout = definitely_outside(p,rvct,BUFF,UseNum,UseMCDI,UseWinding)
  if defin:
	  ins=ins+1
  if defout:
	  outs=outs+1
  if not (defin or defout):
	  neither=neither+1


print("Analytic took --- %s seconds ---" % (time.time() - start_time))
print(str(ins)+" are in and "+str(outs)+" are out and "+str(neither)+" are neither")
