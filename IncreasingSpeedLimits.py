sorted_speed_limits = []

def get_increasing_subsequence_count_nlgn(sequence):
    pass
        

def get_increasing_subsequence_count(sequence):

    subsequence_count_starting_at = [1 for i in range(len(sequence))]
    for i in range(len(sequence)-2,-1,-1):
        search_range = xrange(i+1,len(sequence)) 
        for j in search_range:
            if sequence[j] > sequence[i]:
                    subsequence_count_starting_at[i] += (subsequence_count_starting_at[j])
   
    return sum(subsequence_count_starting_at)%1000000007


if __name__ == '__main__':
    
   testcases = int(raw_input())
   
   for testcase in xrange(1, testcases+1):

        n, m, X, Y, Z = map(lambda x: int(x),raw_input().split())
        A = [0 for i in range(m)]
        for i in range(m):
            A[i] = int(raw_input())
        speed_limits = []
        for i in range(n):
            speed_limits.append(A[i % m])
            A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z
        
        min_speed_limit = min(speed_limits)
        speed_limits = map(lambda x: x-min_speed_limit, speed_limits)
        
        
        sorted_speed_limits = [(speed_limits[i],i) for i in range(len(speed_limits))]
        sorted_speed_limits.sort(key=lambda x:x[0])
        
        
        print 'Case #'+ str(testcase) + ': ' + str(get_increasing_subsequence_count(speed_limits))