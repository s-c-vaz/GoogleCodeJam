

if __name__ == '__main__':
    

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        max_shyness, shyness_scores = raw_input().split(' ')
        max_shyness = int(max_shyness)
        shyness_scores = map(lambda x: int(x), list(shyness_scores))
        
        stood_so_far = 0
        people_to_bring = 0
        for i in xrange(0,len(shyness_scores)):
            if i > stood_so_far:
                difference = i - stood_so_far
                people_to_bring += difference
                stood_so_far += difference
                
            stood_so_far += shyness_scores[i]
        
        print 'Case #'+ str(testcase) + ': ' + str(people_to_bring)
