

if __name__ == '__main__':
    
    
        testcases = int(raw_input())
        
        for testcase in xrange(1, testcases+1):

            N, V, X = raw_input().split()
            N = int(N)
            V = float(V)
            X = float(X)
            source_parameters = []
            for i in xrange(0,N):
                R_i, C_i = raw_input().split()
                R_i = float(R_i)
                C_i = float(C_i)
                source_parameters.append((R_i,C_i))
                
            print 'Case #'+ str(testcase) + ': ' 