'''
Created on 31-Aug-2016

@author: annervaz
'''

parties = [0 for _ in range(27)]

def evacuate(party_counts, sequence):
    
    if party_counts.count(0) == len(party_counts):
        return sequence
    
    for i in range(len(party_counts)):
        if 2*party_counts[i] > sum(party_counts):
            return None
    
    for i in range(len(party_counts)):
        if party_counts[i] > 0:
            party_counts[i] -= 1
            for j in range(len(party_counts)):
                if party_counts[j] > 0:
                    party_counts[j] -= 1
                    result = evacuate(party_counts, sequence+[parties[i]+parties[j]])
                    if result != None:
                        return result
                    party_counts[j] += 1
            result = evacuate(party_counts, sequence+[parties[i]])
            if result != None:
                return result
            party_counts[i] += 1

if __name__ == '__main__':
    
    import string
    for x, y in zip(range(0, 26), string.ascii_uppercase):
        parties[x] = str(y)
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        N = int(raw_input())
        party_counts = map(lambda x: int(x), raw_input().split())

        print 'Case #'+ str(testcase) + ': ' + ' '.join(evacuate(party_counts, []))