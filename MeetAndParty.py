import math, copy, itertools

def get_points(rectangular_area):
    
    return list(itertools.product(xrange(rectangular_area[0],rectangular_area[2]+1),xrange(rectangular_area[1],rectangular_area[3]+1)))

def compute_distance_sum(points, which_key=lambda x: x[0]):
    
    sorted_points = []
    for i in xrange(len(points)):
        sorted_points.append((which_key(points[i]),i))
    
    sorted_points.sort(key=lambda x:x[0])
    
    L = [sorted_points[i][0] for i in xrange(len(sorted_points))]
    R = [sorted_points[i][0] for i in xrange(len(sorted_points))]
    
    for i in xrange(1, len(sorted_points)):
        L[i] += L[i-1]
        
    for i in xrange(len(sorted_points)-2,-1,-1):
        R[i] += R[i+1]
        
    distance_sum = [0 for i in xrange(len(sorted_points))]

    for i in xrange(len(sorted_points)):
        
        if i == len(sorted_points)-1:
            R_right = 0
        else:
            R_right = R[i+1]
            
        if i == 0:
            L_left = 0
        else:
            L_left = L[i-1]

        distance_sum[sorted_points[i][1]] = R_right-L_left-((len(sorted_points)-1-2*i)*sorted_points[i][0])
        
    return distance_sum
            

def identify_optimal_meeting_point(points):
    
    x_distance_sum = compute_distance_sum(points, lambda x: x[0])
    y_distance_sum = compute_distance_sum(points, lambda x: x[1])
    total_distance_sum = [sum(x) for x in zip(x_distance_sum, y_distance_sum)]
    
    minimum_distance_sum = float('inf')
    minimum_distance_point = (float('inf'),float('inf'))
    
    for i in xrange(len(points)):
        
        if total_distance_sum[i] < minimum_distance_sum:
            minimum_distance_sum = total_distance_sum[i]
            minimum_distance_point = points[i]
        elif total_distance_sum[i] == minimum_distance_sum:
            if minimum_distance_point[0] > points[i][0]:
                 minimum_distance_point = points[i]
            elif minimum_distance_point[0] == points[i][0] and minimum_distance_point[1] > points[i][1]:
                minimum_distance_point = points[i]
    
    return str(minimum_distance_point[0]) + ' ' + str(minimum_distance_point[1]) + ' ' + str(int(minimum_distance_sum))
    
if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        rectangular_areas_count = int(raw_input())
        rectangular_areas = []
        points = []
        for i in range(rectangular_areas_count):
            
            x1,y1,x2,y2 = map(lambda x: int(x), raw_input().split(' '))
            rectangular_areas.append((x1,y1,x2,y2))
            points.extend(get_points((x1,y1,x2,y2)))
            
        points = list(set(points))
        
        print 'Case #'+ str(testcase) + ': ' + str(identify_optimal_meeting_point(points))