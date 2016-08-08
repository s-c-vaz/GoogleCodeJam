'''
Created on 02-Apr-2016

@author: annervaz
'''

if __name__ == '__main__':
    
    
    
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        D,K,N = map(int,raw_input().split())
        
        floor = [i for i in xrange(1,D+1)]
        N = N%D
        
        for i in xrange(1,N+1):
            
            if i%2 == 1:
                for j in xrange(0,D,2):
                    temp = floor[j]
                    floor[j] = floor[j+1]
                    floor[j+1] = temp
            else:
                temp = floor[0]
                floor[0] = floor[D-1]
                floor[D-1] = temp
                for j in xrange(D-2,0,-2):
                    temp = floor[j]
                    floor[j] = floor[j-1]
                    floor[j-1] = temp
            #print floor
                    
        index_k = floor.index(K)
        print 'Case #'+ str(testcase) + ': ' + str(floor[(index_k+1)%D]) + ' ' + str(floor[(index_k-1)%D])
                
                    