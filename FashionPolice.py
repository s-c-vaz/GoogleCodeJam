'''
Created on 31-Aug-2016

@author: annervaz
'''

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        J, P, S, K = map(lambda x: int(x), raw_input().split())
        
        results = []
        for jacket in range(1,J+1):
            for pants in range(1,P+1):
                for shirt in range(1,min(K+1,S+1)):
                    results.append((jacket,pants,(jacket + pants + shirt) % S+1))
        
        
        print 'Case #'+ str(testcase) + ': ' + str(len(results))
        for combination in results:
            print ' '.join(map(lambda x: str(x), combination))