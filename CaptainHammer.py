import math


if __name__ == '__main__':
    

    G = 9.8
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        V, D = raw_input().split(' ')
        V = float(V)
        D = float(D)
        
        theta = math.degrees(0.5 * math.asin(min(1,(G*D)/(V*V))))
        
        print 'Case #'+ str(testcase) + ': ' + str(theta)
