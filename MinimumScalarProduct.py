
if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        dimension = int(raw_input())
        vector1 = raw_input().split(' ')
        vector2 = raw_input().split(' ')
        
        vector1 = map(lambda x: int(x), vector1)
        vector2 = map(lambda x: int(x), vector2)
        
        vector1.sort()
        vector2.sort(reverse=True)
    
        sum = reduce(lambda x,y: x+y, map(lambda x: x[0]*x[1],zip(vector1,vector2)))
        
        print 'Case #'+ str(testcase) + ': ' + str(sum)