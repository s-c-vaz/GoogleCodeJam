import math

def find_minimum_time_to_eat(pancakes_count):
    
    minimum_time = max(pancakes_count)
    for i in xrange(1, max(pancakes_count)):
        time_taken_to_rearrange = 0
        for j in xrange(0,len(pancakes_count)):
            if pancakes_count[j] > i:
                time_taken_to_rearrange += math.floor((pancakes_count[j]-i)/i)
                if (pancakes_count[j]-i)%i > 0:
                    time_taken_to_rearrange += 1
        minimum_time = min(minimum_time,time_taken_to_rearrange+i)
        
    return int(minimum_time)

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        N = int(raw_input())
        pancakes_count = map(lambda x: int(x),raw_input().split())
        
        print 'Case #'+ str(testcase) + ': ' + str(find_minimum_time_to_eat(pancakes_count)) 