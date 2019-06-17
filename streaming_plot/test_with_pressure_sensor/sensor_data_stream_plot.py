# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:53:04 2019

@author: ventilator
"""

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

import serial
try:
    ser = serial.Serial("COM33")
except:
    ser.close()
    ser = serial.Serial("COM33")

def get_temperature_from_sensor():
#    try:
    while True:
        line = ser.readline() # '26 degrees of Celsius'
        print(line)
        if "Celsius" in str(line):
            return int(line.split()[0])
#    except:
#        ser.close()             # close port
#        raise

def get_pressure_from_sensor():
    while True:
        line = ser.readline()
        print(line)
        if "Pascal" in str(line):
            return int(line.split()[0])

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax2 = ax.twinx()
xs = []
ys = []
y2s = []

max_data_points = 40


# This function is called periodically from FuncAnimation
def animate(i, xs, ys, y2s):

    # Read temperature (Celsius) from TMP102
    temp_c = round(random.random()*25)
    temp_c = get_temperature_from_sensor()
    pressure_p = get_pressure_from_sensor()
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
#    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(temp_c)
    y2s.append(pressure_p)
    # Limit x and y lists to max_data_points items
    xs = xs[-max_data_points:]
    ys = ys[-max_data_points:]
    y2s = y2s[-max_data_points:]
    # Draw x and y lists
    ax.clear()
    ax2.clear()
    
    color = 'tab:blue'
    ax2.set_ylabel("Pressure")   
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.ticklabel_format(axis='y', style='plain') # does not work
    ax2.plot(xs, y2s, color=color)     
 
    color = 'tab:red'
    ax.set_ylabel("Temperature (deg C)")
    ax.plot(xs, ys, color=color)    
    ax.tick_params(axis='y', labelcolor=color)    
    
    ax.tick_params(axis='x', rotation=45) 
    
    # Format plot
#    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Sensor value over Time')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, y2s), interval=1000)
plt.show()
