import math

def get_traingle_properties(points):

    sides_squares = []
    result = ''
    
    for i in xrange(len(points)):
        for j in xrange(i+1,len(points)):
            sides_squares.append(((points[i][1]-points[j][1])*(points[i][1]-points[j][1]))+((points[i][0]-points[j][0])*(points[i][0]-points[j][0])))
       
    if (points[0][1] - points[1][1]) * (points[0][0] - points[2][0]) == (points[0][1] - points[2][1]) * (points[0][0] - points[1][0]):
        return 'not a triangle'
    
    if sides_squares[0] == sides_squares[1] and sides_squares[1] == sides_squares[2]:
        result += 'equilateral '
    elif sides_squares[0] == sides_squares[1] or sides_squares[1] == sides_squares[2] or sides_squares[0] == sides_squares[2]:
        result += 'isosceles '
    else:
        result += 'scalene '
        
    sides_squares.sort(reverse=True)
    
    check_value = sides_squares[2]+sides_squares[1]-sides_squares[0]
    
    if check_value < 0:
        result += 'obtuse '
    elif check_value == 0:
        result += 'right '
    else:
        result += 'acute '
    
    result += 'traingle'
    return result

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        coordinates = raw_input().split()
        coordinates = map(lambda x: int(x), coordinates)
        points = [(coordinates[0],coordinates[1]),(coordinates[2],coordinates[3]),(coordinates[4],coordinates[5])]

        print 'Case #'+ str(testcase) + ': ' + get_traingle_properties(points)