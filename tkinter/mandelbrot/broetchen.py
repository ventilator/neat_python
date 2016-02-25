# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import tkinter as tk
from numba import autojit

class mandelbrot():
    boundary = 2.0
    boundary_squared = boundary * boundary
        
    def f(self, z, c):
        return z*z + c
            
    def calculate(self, c):    
        z0 = 0 + 0*1j
        z = z0     
        
        for i in range(20):        
            z = self.f(z, c)
            # if abs(z) > self.boundary: # next line yields same result, but is a bit faster (https://www.ibm.com/developerworks/community/blogs/jfp/entry/How_To_Compute_Mandelbrodt_Set_Quickly?lang=en)
            if z.real * z.real + z.imag * z.imag > self.boundary_squared:
                return i
        
        return 0
        

# function is 10x faster than class above. Class above does not accept autojit for unknown reason
@autojit
def mandel(x, y, max_iters):
  c = complex(x, y)
  z = 0.0j
  for i in range(max_iters):
    z = z*z + c
    if (z.real*z.real + z.imag*z.imag) >= 4:
      return i
  return max_iters

      
class calculator():
    def generate_broetchen(self, x_points, y_points, bounding_box = [-1.75, 0.5, -1, 1]):
        
        # mb = mandelbrot()
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
                # disabled slower variant 
                    # c = c_re_current + c_im_current*1j                
                    # grid[x,y] = mb.calculate(c)
                grid[x,y] = mandel(c_re_current, c_im_current, 20)
     
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
                    


#if __name__ == "__main__":
#    root = tk.Tk()
#    Renderer(root).pack(fill="both", expand=True)
#    root.mainloop()
    
def test_run():
    mandala = calculator()        
    data = mandala.generate_broetchen(200, 200)    
    
#if __name__ == '__main__':    
#    import profile 
#    profile.run('test_run()')   
    
    #930295 function calls in 3.011 seconds
    
if __name__ == '__main__':   
    from timeit import default_timer as timer
    start = timer()
    
    test_run()
    
    dt = timer() - start
    print ("Mandelbrot created in %f s" % dt)
    
  



