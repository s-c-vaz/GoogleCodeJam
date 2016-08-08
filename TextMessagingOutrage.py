
def get_optimal_placement_keypadpress_count(P, K, L, frequencies):
    
    keypadpress_count = 0
    num_presses = 1
    alloted_letters = 0
    while alloted_letters < L:
        press = 0
        while (press < K) and (alloted_letters < L):
            max_frequencies = max(frequencies)
            frequencies[frequencies.index(max_frequencies)] = -1
            keypadpress_count += (num_presses*max_frequencies)
            alloted_letters += 1
            press += 1
        num_presses += 1
        
    return keypadpress_count

if __name__ == '__main__':
    
   testcases = int(raw_input())
   
   for testcase in xrange(1, testcases+1):

        P, K, L = raw_input().split()
        P = int(P)
        K = int(K)
        L = int(L)
        frequencies = raw_input().split()
        frequencies = map(lambda x: int(x), frequencies)
        
        print 'Case #'+ str(testcase) + ': ' + str(get_optimal_placement_keypadpress_count(P,K,L,frequencies))