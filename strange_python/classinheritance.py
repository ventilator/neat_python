# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:44:03 2016

@author: gruenewa
"""

class Shape():
    counter = 0   
    def __init__(self):
        print("init shape", self.counter)        
    
    def increase(self):        
        self.counter +=1  
        print("increasing", self.counter)

    def print_counter(self):
        print("printing by print", self.counter)

    def create_child(self):
        # Create Circle and increase.
        c = Circle()
        c.increase()
        c2 = Circle2()
        c2.increase()

class Circle(Shape):
    def increase(self):
        # Call method from parent class.
        super().increase()
        Shape.counter = 5
        print("set to 5")
        
        
class Circle2(Shape):
    def increase(self):
        # Call method from parent class.
        super().increase()
        print("increase by one (circle2)")
       

s = Shape()
s.create_child()
s.print_counter()
print("end")