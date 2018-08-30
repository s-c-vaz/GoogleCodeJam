'''
Created on 30-Aug-2018

@author: annervaz
'''
from numpy import inf


def get_cruise_control_speed(horses,destination):
 
    clock = 0
    
    horses.append((destination,0))
    
    horses.sort(key=lambda x: x[0])
    
    while len(horses) > 1:
        
        min_time = inf
        min_time_horse_index = -1
        for i in range(len(horses)-1):
            if (horses[i][1] - horses[i+1][1]) > 0:
                t = (horses[i+1][0] - horses[i][0])/(horses[i][1] - horses[i+1][1])
                if t < min_time:
                    min_time = t
                    min_time_horse_index = i
                    
        if min_time_horse_index != -1:
            
            clock += min_time
            horses = horses[:min_time_horse_index] + horses[min_time_horse_index+1:]
            horses = list(map(lambda x: (x[0]+min_time*x[1],x[1]),horses))
            horses[len(horses)-1] = (destination,0)
            
        else:
            
            max_time = ((destination-horses[0][0])/horses[0][1]) + clock
            return destination/max_time
            
    
    max_time = clock
    return destination/max_time


if __name__ == '__main__':

    testcases = int(input())
    for testcase in range(1, testcases+1):
        destination, numHorses = list(map(lambda x: int(x), input().split()))
        horses = []
        for _ in range(1,numHorses+1):
            horse_position, horse_speed = list(map(lambda x: int(x), input().split()))
            horses.append((horse_position, horse_speed))
            
        print('Case #'+ str(testcase) + ': ' + "{:.6f}".format(get_cruise_control_speed(horses,destination)))