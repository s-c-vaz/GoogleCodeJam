def min_flips_to_configure(current_flows, required_flows):
    
    flip_patterns = [[] for x in xrange(len(required_flows))]
    for i in xrange(len(required_flows)):
        for j in xrange(len(current_flows)):
            flips = ['0' if required_flows[i][k] == current_flows[j][k] else '1' for k in xrange(len(required_flows[i]))]
            flip_patterns[i].append((''.join(flips),j))
            
    intersections = []

    for flip_pattern1 in flip_patterns[0]:
        exist_in_all = True 
        for i in xrange(1, len(required_flows)):
            found = False
            for flip_pattern2 in flip_patterns[i]:
                if flip_pattern1[0] == flip_pattern2[0] and flip_pattern1[1] != flip_pattern2[1]:
                    found = True
                    break
            if not found:
                exist_in_all = False
                break
        if exist_in_all:
            intersections.append(flip_pattern1[0])
           
    if len(intersections) == 0:
        return None
    
    flips_in_intersection = map(lambda x: x.count('1'), intersections)
    
    return min(flips_in_intersection)
                
                


if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        N, L = map(lambda x: int(x), raw_input().split(' '))
        
        current_flows = raw_input().split(' ')
        required_flows = raw_input().split(' ')
        

        num_flips_required = min_flips_to_configure(current_flows, required_flows)
        if num_flips_required == None:
            print 'Case #'+ str(testcase) + ': ' + 'NOT POSSIBLE'
        else:
            print 'Case #'+ str(testcase) + ': ' + str(int(num_flips_required))