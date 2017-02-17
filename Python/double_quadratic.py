"""
double_quadratic - checking properties of the extrema of a double quadratic over a
                   rectangular region

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

import math
from quad_minmax import *

AE = 0.00000001



def ae(a,b):
    return (abs(a-b)<AE)

def sq(a):
    return a*a

def discr(a,b,c):
    return b**2-4*a*c

def root(a,b,c,eps):
    return (-b+eps*math.sqrt(discr(a,b,c)))/(2*a)

def quad(a,b,c,d,ee,f,x,y):
    return a*sq(x)+b*sq(y)+c*x*y+d*x+ee*y+f

def rev_disc(a,b,c):
    return sq(c)-4*a*b

def quad_min_y_to_x(a,c,d,y):
    return -(c*y+d)/(2*a)

def quad_min_y(a,b,c,d,ee):
  if ae(rev_disc(a,b,c),0):
      return 0
  else:
      return (2*a*ee-c*d)/rev_disc(a,b,c)

def quad_min_x(a,b,c,d,ee):
  if ae(rev_disc(a,b,c),0):
      return 0
  else:
    return (2*b*d-c*ee)/rev_disc(a,b,c)

def quad_min_unit_box_init(a,b,c,d,ee,f,D):
  if quad_min_le_D_int(a,c*1+d,quadratic(b,ee,f,1),0,1,D):
      return True
  if quad_min_le_D_int(a,d,f,0,1,D):
      return True
  if quad_min_le_D_int(b,c*1+ee,quadratic(a,d,f,1),0,1,D):
      return True
  if quad_min_le_D_int(b,ee,f,0,1,D):
      return True
  mx = quad_min_x(a,b,c,d,ee)
  my = quad_min_y(a,b,c,d,ee)
  if (0<=mx and mx<=1 and 0<=my and my<=1 and quad(a,b,c,d,ee,f,mx,my)<D):
      return True
  return False

def quad_min_unit_box(a,b,c,d,ee,f,D):
  if quad_min_le_D_int(a,c*1+d,quadratic(b,ee,f,1),0,1,D):
      return True
  if quad_min_le_D_int(a,d,f,0,1,D):
      return True
  if quad_min_le_D_int(b,c*1+ee,quadratic(a,d,f,1),0,1,D):
      return True
  if quad_min_le_D_int(b,ee,f,0,1,D):
      return True
  if rev_disc(a,b,c)>=0:
      return False
  mx = (2*b*d-c*ee)
  my = (2*a*ee-c*d)
  if (0<=mx*rev_disc(a,b,c) and
      mx*rev_disc(a,b,c)<=rev_disc(a,b,c)**2 and 
       0<=my*rev_disc(a,b,c) and
       my*rev_disc(a,b,c)<=rev_disc(a,b,c)**2 and
       quad(a,b,c,d*rev_disc(a,b,c),ee*rev_disc(a,b,c),
            f*rev_disc(a,b,c)**2,mx,my)<D*rev_disc(a,b,c)**2):
      return True
  return False
