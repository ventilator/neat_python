# -*- coding: utf-8 -*-

import tkinter
from PIL import Image, ImageTk
import numpy as np
import time
import broetchen

class mainWindow():
        times=1
        timestart=time.clock()
        dimension_x = 800
        dimension_y = 800

        print("calculating")
        pixelator = 1
        mandala = broetchen.calculator()        
        data = mandala.generate_broetchen(dimension_x/pixelator, dimension_y/pixelator)
        data = data*15
        data = np.rot90(data)
        print("%.02f s done"%(time.clock()-timestart))
        timestart=time.clock()
        print("rendering")
        
        def __init__(self):
                self.root = tkinter.Tk()
                self.frame = tkinter.Frame(self.root, width=self.dimension_x, height=self.dimension_y)
                self.frame.pack()
                self.canvas = tkinter.Canvas(self.frame, width=self.dimension_x, height=self.dimension_y)
                #self.canvas.place(x=-2,y=-2)
                self.canvas.grid(sticky="NSWE")
                self.root.after(0,self.start) # INCREASE THE 0 TO SLOW IT DOWN
                self.root.mainloop()
                
        def start(self):
                global data
                self.im=Image.fromstring('L', (self.data.shape[1],\
                        self.data.shape[0]), self.data.astype('b').tostring()) # creates image with dimensions ("shape") of array
                self.photo = ImageTk.PhotoImage(image=self.im)
                self.canvas.create_image(0,0,image=self.photo,anchor=tkinter.NW)
                self.root.update()
                self.times+=1
                if self.times%33==0:
                        print("%.02f FPS"%(self.times/(time.clock()-self.timestart)))
                #self.root.after(10,self.start)
                #self.data=numpy.roll(self.data,-1,1)
                print("%.02f s done"%(time.clock()-self.timestart))                        

if __name__ == '__main__':
    x=mainWindow()
    