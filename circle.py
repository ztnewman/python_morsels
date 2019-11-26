#!/usr/bin/env python3
import math 

class Circle:
    
    def __init__(self,radius=1):
        if radius < 1:
            raise ValueError('A very specific bad thing happened')
        self.radius = radius 

    def __str__(self):
        return "Circle("+str(self.radius)+")"

    def __repr__(self):
        return "Circle("+str(self.radius)+")"

    @property
    def diameter(self):
        return self.radius*2

    @property
    def area(self):
        return (self.radius**2) * math.pi
 
    @diameter.setter
    def diameter(self,diameter):
        self.diameter = diameter
        self.radius = diameter / 2
