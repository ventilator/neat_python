# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:35:52 2016

@author: gruenewa
"""
import math
import numpy as np
import holoviews as hv 

n = 4
alpha = 2*math.pi/n
edges = []
for i in range(n):
    x = np.array([math.cos(alpha*i), math.sin(alpha*i)])
    print(x)
    
    
r = np.arange(0, 1, 0.005)
xs, ys = (r * fn(85*np.pi*r) for fn in (np.cos, np.sin))
paths = hv.Points((xs, ys))
paths + paths[0:1, 0:1]    