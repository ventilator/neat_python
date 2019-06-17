# -*- coding: utf-8 -*-
"""
@author: ventilator
"""
import collections 
import seaborn as sns
import matplotlib.pyplot as plt
import csv

import pickle

class read_file():
    def testfile(self,name):
        c = collections.Counter()
        
        with open(name, 'r') as f:
            for s in f:            
                u, p = s.split(":")
                if len(p) == 7:
                    p = p.strip()
#                    print(p)
                    c.update(p)
        return c
        print(c.most_common(10))
     
    def plot_digits(self,c):
        data = c.most_common(10)
        sns.scatterplot(data=data)
        
    def collection_to_file(self,c,name):
        with open(name, "wb") as f:
            w = csv.writer(f)
            print(type(c.most_common()))
            w.writerows(c.most_common())
            
    def pickle_(self,c,name):
        with open(name, "wb") as f:
            pickle.dump(c,f)                   
            
    def unpickle_(self,name):    
        with open(name, "rb") as f:
            return pickle.load(f)          
        
def solve_problem():
    rf = read_file()
#    collection_ = rf.testfile("random.txt")  
#    rf.collection_to_file(collection_,"result.csv")
#    rf.pickle_(collection_,"result")
    collection_ = rf.unpickle_("result")
    print(collection_)
#    rf.plot_digits(collection_)      
        
if __name__ == "__main__":    
    import time
    start_time = time.time()         
    solve_problem()  
    print("runtime: \x1b[1;31m%.1fs\x1b[0m" % (time.time() - start_time))      