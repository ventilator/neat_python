# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt

class mandelbrot():
    def calculate(self, z, c):
        return z*z + c
        
        
        
        
def main():
    boundary = 2.0
    mb = mandelbrot()
    c_re_min = -2
    c_re_max = 2
    c_im_min = -1
    c_im_max = 1
    points = 100
    # grid = np.zeros((points, points))
    c_re = np.linspace(c_re_min, c_re_max, num=points)
    c_im = np.linspace(c_im_min, c_im_max, num=points)
    
    grid_x = []
    grid_y = []
    grid_color = []
    
    x = -1    
    y = -1
    for c_re_current in c_re:
        x += 1
        y = -1
        for c_im_current in c_im:
            y += 1            
            z0 = 0 + 0*1j
            z = z0
            c = c_re_current + c_im_current*1j
            for i in range(20):        
                z = mb.calculate(z, c)
                if abs(z) > boundary:
                    break
                
            grid_x.append(c_re_current)    
            grid_y.append(c_im_current)
            if abs(z) > boundary:                                        
                grid_color.append(1)
            else:
                grid_color.append(0)                
 
    
    
    plt.scatter(grid_x, grid_y, c=grid_color, alpha=0.5)
    plt.show()

main()        