import math, sys

def calculate_time(C,F,X,P):

    time_to_get_to_C = C/P

    time = 0
    while (time_to_get_to_C + (X/(P+F))) < (X/P):
        
        P += F
        time += time_to_get_to_C
        time_to_get_to_C = C/P
        
    time += (X/P)
    
    return time
    

if __name__ == '__main__':
    
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        C, F, X = map(lambda x: float(x), raw_input().split(' '))
        
        print 'Case #'+ str(testcase) + ': ' + str(calculate_time(C,F,X,2))

