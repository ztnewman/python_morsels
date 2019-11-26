#!/usr/bin/env python3

class Point:
    
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z 

    def __str__(self):
        return "Point(x="+str(self.x)+", y="+str(self.y)+", z="+str(self.z)+")"

    def __repr__(self):
        return "Point(x="+str(self.x)+", y="+str(self.y)+", z="+str(self.z)+")"


    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y, self.z+point.z)

    def __sub__(self, point):
        return Point(self.x-point.x, self.y-point.y, self.z-point.z)

    def __mul__(self, scale):
        return Point(self.x*scale, self.y*scale, self.z*scale)

    def __rmul__(self, scale):
        return Point(self.x*scale, self.y*scale, self.z*scale)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y) and (self.z == other.z):
            return True
        else: 
            return False

    def __iter__(self):
        yield self.x 
        yield self.y 
        yield self.z

