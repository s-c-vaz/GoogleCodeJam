'''
Created on 22-Jan-2016

@author: annervaz
'''

if __name__ == '__main__':
   
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        N = int(raw_input())
        M = int(raw_input())
        customers_pref = []
        satisfied_customers = [(i,[],[]) for i in xrange(0,N)]
        for i in xrange(0,M):
            customers_pref.append(map(lambda x: int(x), raw_input().split()))
        for j,element in enumerate(customers_pref):
            for i in xrange(1,len(element),2):
                satisfied_customers[element[i]-1][element[i+1]+1].append(j)
        
        answer = [0 for i in xrange(0,N)]
        customers = []
        impossible = False
        
        
        while len(customers) < M:
        
            satisfied_customers = map(lambda x: (x[0],list(set(x[1])-set(customers)),list(set(x[2])-set(customers))),satisfied_customers)
            new_customers_possible = reduce(lambda x,y: x+y,map(lambda x: len(x[1]),satisfied_customers))
            new_customers_possible += reduce(lambda x,y: x+y,map(lambda x: len(x[2]),satisfied_customers))
            if new_customers_possible == 0:
                impossible = True
                break
            satisfied_customers.sort(key=lambda x: (len(x[2]),len(x[1])), reverse=True)
            current_shake_config = satisfied_customers[0]
            satisfied_customers = satisfied_customers[1:]
            future_unmalted_customers = []
            map(lambda x: future_unmalted_customers.extend(x[1]),satisfied_customers)
            future_unmalted_customers = list(set(future_unmalted_customers))
            malted_unique = False
            for x in current_shake_config[2]:
                if x not in future_unmalted_customers:
                    malted_unique = True
                    customers.extend(current_shake_config[2])
                    answer[current_shake_config[0]] = 1
                    break
            if not malted_unique:
                customers.extend(current_shake_config[1])
                
            customers = list(set(customers))
            
            if len(satisfied_customers) == 0 and len(customers) < M:
                impossible = True
                break
                             
        if impossible:
            print 'Case #'+ str(testcase) + ': IMPOSSIBLE'
        else:
            answer = reduce(lambda x,y: str(x) + ' ' + str(y), answer)
            print 'Case #'+ str(testcase) + ': ' + str(answer)
                    
            
        