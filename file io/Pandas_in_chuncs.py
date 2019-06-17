# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:29:45 2019

@author: gruenewa
"""

import pandas as pd
import re 
import numpy as np
import seaborn as sns
import sys

def readfile(filename):
    chunksize = 200000  
    
    results = []
    for c in pd.read_csv(filename, sep=":", header=None, names=["user","password","hint"],chunksize=chunksize):
        print(c.head())
        ints = filter_int(c,digits=6)
        results.append(ints)
        break
    result = pd.concat(results)
    print(result.head())
    print(result.tail())
    plot_int(result)
        
def filter_int(data,digits):
    # use regex, in particular re.match, which search the beginning of a string only (in contrast to re.search)
    filtered = data.password.str.match(r'\d{6}')
    filter_data = data[filtered]
#    print(data[filtered].head())
    return filter_data
       
def plot_int(data):
    statistical_data = data.password.value_counts()
    print(statistical_data.head())
    print(statistical_data[0])
    sys.exit('Ende')
    sns.set(style="ticks")
    fig = sns.jointplot(statistical_data, kind="hex", color="#4CB391")                    
    fig.set_axis_labels('Anzahl LEDs pro Klammer', 'Lötdauer [min]')

def solve_problem():
    readfile("random.txt")      
        
if __name__ == "__main__":    
    import time
    start_time = time.time()         
    solve_problem()  
    print("runtime: \x1b[1;31m%.1fs\x1b[0m" % (time.time() - start_time))  