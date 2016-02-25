# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


class mandelbrot():
    def calculate(self, z, c):
        return z*z + c
        
        
class calculator():
    def generate_broetchen(self, x_points, y_points, bounding_box = [-1.75, 0.5, -1, 1]):
        boundary = 2.0
        mb = mandelbrot()
        c_re_min, c_re_max, c_im_min, c_im_max = bounding_box
        
        grid = np.zeros((x_points, y_points))
        c_re = np.linspace(c_re_min, c_re_max, num=x_points)
        c_im = np.linspace(c_im_min, c_im_max, num=y_points)

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
                
                if abs(z) > boundary:                                      
                    grid[x,y] = 1
                else:              
                    grid[x,y] = 0
     
        return grid        
        

# old renderer, use render.py instead
class Renderer(tk.Frame):
    def __init__(self, root):
        
        
        
        tk.Frame.__init__(self, root)
        
        c_width = 800
        c_height = 800
        self.canvas = tk.Canvas(self, width=c_width, height=c_height, background="bisque")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        print("calculating")
        pixelator = 4
        mandala = calculator()        
        data = mandala.generate_broetchen(c_width/pixelator, c_height/pixelator)
        print("rendering")

        n_y_points = len(data)        
        y_spacing = c_height / n_y_points
        # print(y_spacing)
        for i_x, x in enumerate(data):
            n_x_points = len(x)
            x_spacing = c_width / n_x_points
            for i, y in enumerate(x):
                # print(i_x, i, data[i_x, i])
                if data[i_x, i] == 0:
                    fillcolor = "lightblue"
                    # print(i_x, i, data[i_x, i])
                else:
                    fillcolor = "bisque"
                self.canvas.create_rectangle(i_x*x_spacing,i*y_spacing, (i_x+1)*x_spacing, (i+1)*y_spacing, fill=fillcolor, tag="rect", width=0)
                    


if __name__ == "__main__":
    root = tk.Tk()
    Renderer(root).pack(fill="both", expand=True)
    root.mainloop()
    
# main()        



