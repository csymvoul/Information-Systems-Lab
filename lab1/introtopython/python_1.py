# Classes

import flask
from flask import Flask
from flask import Flask as F

# This is a single line comment in Python

"""
This is how you 
write a multiple line comment in Python
"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = x
    
    def add_XY(self):
        return self.x+self.y
    
    def set_X(self, x):
        self.x = x
        
    def set_Y(self, y):
        self.y = y
    
    def get_X(self):
        return self.x
    
    def get_Y(self):
        return self.y
    
point = Point(x=1, y=10)
print(point.get_X())