import sys
import math

LARGE_W = int(math.pow(10, 3))
LARGE_B = int(math.pow(10, 3))
ending_balls = []

def initialialize(W,B):
    
    for i in xrange(0,W+B):
        ending_balls.append([-1 for j in xrange(0,B+1)])
        
def get_last_ball_by_numbers(W,B):
    
    if B%2 == 0:
        return 'W'
    else:
        return 'B'

def get_last_ball(W,B):
  
    if ending_balls[W][B] != -1:
        return ending_balls[W][B]
    
    if W == 0 and B == 1:
        ending_balls[W][B] = 'B'
        return ending_balls[W][B]
    elif W == 1 and B == 0:
        ending_balls[W][B] = 'W'
        return ending_balls[W][B]
    
    result1 = None 
    if W>=2 or (W>=1 and B>=1):
        result1 = get_last_ball(W-1,B)
    
    result2 = None  
    if B>=2:
        result2 = get_last_ball(W+1,B-2)

    if result1 != None and result2 != None and result1 != result2:
        ending_balls[W][B] = 'U'
        return ending_balls[W][B]
    else:
        if result1 != None: 
            ending_balls[W][B] = result1
            return ending_balls[W][B]
        elif result2 != None: 
            ending_balls[W][B] = result2
            return ending_balls[W][B]

if __name__ == '__main__':
    
    sys.setrecursionlimit(10000)
    
    ending_balls = []
    initialialize(LARGE_W,LARGE_B)

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        W,B = raw_input().split()
        W = int(W)
        B = int(B)
        
        #result = get_last_ball(W,B) 
        result = get_last_ball_by_numbers(W,B) 
        if result == 'B':
            result = 'BLACK'
        elif result == 'W':
            result = 'WHITE'
        else:
            result = 'UNKNOWN'
            
        print 'Case #'+ str(testcase) + ': ' + result