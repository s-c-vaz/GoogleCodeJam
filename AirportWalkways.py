'''
Created on 23-Dec-2015

@author: annervaz
'''

import math

if __name__ == '__main__':
    
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        X,S,R,T,N = map(lambda x: float(x),raw_input().split(' '))
        N=int(N)
        walkways = []
        total_walkway_length = 0
        for walkway in xrange(1,N+1):
            B,E,W = map(lambda x: float(x),raw_input().split(' '))
            walkways.append([E-B,float(W)])
            total_walkway_length += (E-B)
        walkways.append([X-total_walkway_length,float(0)])
            
        walkways.sort(key=lambda x: x[1])
        
        total_time_taken = 0
        #print walkways
        for walkway in walkways:
            time_taken = walkway[0]/(walkway[1]+R)
            if time_taken > T:
                time_taken = (walkway[0]-((walkway[1]+R)*T))/(walkway[1]+S)
                time_taken += T
                T = 0
            else:
                T -= time_taken
            total_time_taken += time_taken
            
        print 'Case #'+ str(testcase) + ': ' +str(total_time_taken)