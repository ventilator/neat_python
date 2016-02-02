# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:44:03 2016

@author: gruenewa
"""

class Shape:
    counter = 0   
    def increase(self):        
        self.counter +=1        


class Circle(Shape):
    def increase(self):
        # Call method from parent class.
        super().increase()
        
        
class Circle2(Shape):
    def increase(self):
        # Call method from parent class.
        super().increase()
       

# Create Circle and increase.
c = Circle()
c.increase()
c2 = Circle2()
c2.increase()