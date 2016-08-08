'''
Created on 23-Dec-2015

@author: annervaz

answer for both small and large is marked incorrect by judge, precision problem maybe
'''
import numpy as np

def findnthroot(x,n):
       p = [1]
       p.extend([0 for i in xrange(0,n-1)])
       p.append(-1*x)
       roots = np.roots(p)
       isreal = map(lambda x: x==0, roots.imag)
       for i in xrange(0,len(roots.real)):
           if isreal[i]:
               return roots.real[i]
       

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        print 'Case #'+ str(testcase) + ':'
        N,M = map(lambda x: int(x),raw_input().split(' '))
        dimensions = map(lambda x: int(x),raw_input().split(' '))
        for query in xrange(1,M+1):
            L, R = map(lambda x: int(x),raw_input().split(' '))
            dimensions_to_consider = dimensions[L:R+1]
            #print L,R,dimensions,dimensions_to_consider
            volume = reduce(lambda x,y: x*y,dimensions_to_consider)
            print str(findnthroot(volume, len(dimensions_to_consider)))