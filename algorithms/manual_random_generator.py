# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:16:00 2017

@author: gruenewa

https://cdsmith.wordpress.com/2011/10/10/build-your-own-simple-random-numbers/
"""

seed = 1
def radum():
    global seed
    i = seed
    b = 7*i % 101
    n = (b-1) % 10 +1
    seed = n
    return n


seed = 3
m = radum(seed)
for i in range(20):
    print(m)
    m = radum()/10*8-4