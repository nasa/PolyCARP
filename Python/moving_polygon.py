"""
moving_polygon - data structure for a moving 2D polygon

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

from vectors import *
class MovingPolygon:
    
    def __init__(self, polystart = [Vector(0,0)], polyvel = [Vector(0,0)]):
        self.polystart = polystart
        self.polyvel = polyvel
        
    def __str__(self):
        return "( polystart:= " + str(self.polystart) + ", polyvel:= " + str(self.polyvel) + ")"

    def at(self,t):
        ans=[]
        for i in range(0,len(self.polystart)):
            ans.append(self.polystart[i]+(self.polyvel[i]*t))
        return ans

