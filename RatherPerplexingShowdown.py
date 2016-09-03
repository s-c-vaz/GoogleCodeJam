'''
Created on 31-Aug-2016

@author: annervaz
'''

def solve(N,R,P,S):
    
    a = 'P'
    b = 'R'
    c = 'S'
    
    for i in range(N):
        a,b,c = a+b,a+c,b+c
        
    for alignment in a,b,c:
        
        if alignment.count('P') == P and alignment.count('R') == R and alignment.count('S') == S:
            return  alignment
        
    return 'IMPOSSIBLE'
    

if __name__ == '__main__':
    
    
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        N, R, P, S = map(lambda x: int(x), raw_input().split())
        
        result = solve(N, R, P, S)
        print 'Case #'+ str(testcase) + ': ' + result