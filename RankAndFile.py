'''
Created on 29-Aug-2016

@author: annervaz
'''
 

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        N = int(raw_input())
        lists = []
        for i in range(0,2*N-1):
            new_list = map(lambda x: int(x),raw_input().split())
            lists.extend(new_list)
           
        answer = []
        for i in range(len(lists)):
            if lists.count(lists[i]) % 2 != 0:
                answer.append(lists[i])
        answer = list(set(answer))
        answer.sort()
        print 'Case #'+ str(testcase) + ': ' + ' '.join(map(lambda x: str(x),answer))
