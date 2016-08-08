
def count_intervals(value, intervals):
    
    result = 0
    for interval in intervals:
        if value in xrange(interval[0],interval[1]+1):
            result += 1
            
    return result


if __name__ == '__main__':
    

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        GBuses = int(raw_input())
        routes = map(lambda x: int(x), raw_input().split())
        covered = []
        for i in xrange(0,GBuses*2,2):
            covered.append((routes[i],routes[i+1]))
        queries = []
        query_count = int(raw_input())
        for i in xrange(0,query_count):
            queries.append(int(raw_input()))
    

        values = map(lambda x: count_intervals(x,covered),queries)
        values = reduce(lambda x, y : str(x) + ' ' + str(y), values)
            
        print 'Case #'+ str(testcase) + ': ' + values
        raw_input()
