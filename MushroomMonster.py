def get_count_1(mushroom_counts):
    
    count = 0
    
    for i in xrange(1,len(mushroom_counts)):
        diff = mushroom_counts[i-1] - mushroom_counts[i]
        if diff > 0:
            count += diff
            
    return count
    
    
    
def get_count_2(mushroom_counts):
    
    
    largest_count_eaten_in_an_interval = 0
    
    for i in xrange(0,len(mushroom_counts)-1):
        if (mushroom_counts[i] - mushroom_counts[i+1]) > largest_count_eaten_in_an_interval:
            largest_count_eaten_in_an_interval = mushroom_counts[i] - mushroom_counts[i+1]
            
    count = 0
    for i in xrange(0,len(mushroom_counts)-1):
        if mushroom_counts[i] > largest_count_eaten_in_an_interval:
            count += largest_count_eaten_in_an_interval
        else:
            count += mushroom_counts[i]


    return count

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        N = int(raw_input())
        mushroom_counts = map(lambda x: int(x),raw_input().split())
        print 'Case #'+ str(testcase) + ': ' + str(get_count_1(mushroom_counts)) + ' ' +str(get_count_2(mushroom_counts))