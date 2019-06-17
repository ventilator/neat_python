# -*- coding: utf-8 -*-
"""
@author: ventilator
"""
import random
import string

class gen_file():
    def testfile(name):
        N=10
        M=1000000
        with open(name, 'w') as f:
            for i in range(M):
                NN = random.randint(N,N+8)
                s = ''.join(random.choices(string.ascii_lowercase + string.digits, k=NN))
                if NN % 2 == 0:
                    # random
                    p = ''.join(random.choices(string.ascii_lowercase + string.digits, k=NN-4))
                else:
                    # 6 digit
                    p = ''.join(random.choices(string.digits, weights=[9,2,4,2,1,1,1,1,7,8], k=6))
                s = s+'@xyz.ab:'+p+'\n'
                f.write(s)
        
        
def solve_problem():
    gf = gen_file
    gf.testfile("random.txt")        
        
if __name__ == "__main__":    
    import time
    start_time = time.time()         
    solve_problem()  
    print("runtime: \x1b[1;31m%.1fs\x1b[0m" % (time.time() - start_time))       