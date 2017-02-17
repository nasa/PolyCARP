"""
vectors - a very simple 2D vectors library

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

import math
from double_quadratic import *

def prlist(l):
    ans = "["
    for i in range(len(l)):
        ans = ans+str(l[i])+","
    ans = ans[0:len(ans)-1]
    ans = ans+"]"
    return ans

class Vector:
    
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, val):
        return VectPoint( self.x + val.x, self.y + val.y )
    
    def __sub__(self,val):
        return VectPoint( self.x - val.x, self.y - val.y )

    def __div__(self, val):
        return VectPoint( self.x / val, self.y / val )
    
    def __mul__(self, val):
        return VectPoint( self.x * val, self.y * val )
                
    def __getitem__(self, i):
        if( i == 0):
            return self.x
        elif( i == 1):
            return self.y
        else:
            raise Exception("Invalid i to VectPoint")
        
    def __setitem__(self, i, value):
        if( i == 0):
            self.x = value
        elif( i == 1):
            self.y = value
        else:
            raise Exception("Invalid i to VectPoint")
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def dot(self,other):
        return self.x*other.x+self.y*other.y

    def norm(self):
        return math.sqrt(self.sqv())

    def sqv(self):
        ans = self.x**2+self.y**2
        return ans

    def Scal(self,val):
        return self*val

    def AddScal(self,val,other):
        return self+other.Scal(val)

    def perpR(self):
        return VectPoint(self.y,-self.x)

    def det(self,other):
        return self.dot(other.perpR())

    def ae(self,other):
        return (ae(self.x,other.x) and ae(self.y,other.y))

    def hat(self):
        if self.norm()==0: return self
        return self.Scal(1/self.norm())

    def topair(self):
        return (self.x,self.y)

    def topvs(self):
        return "(# x:= "+str(self.x)+", y:= "+str(self.y)+" #)"
    
VectPoint = Vector
