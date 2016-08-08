def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
def lcm_by_gcd(numbers):
    
    return reduce(lambda x, y: x * y/GCD(x,y), numbers)


def allocate(time_to_be_free, M_ks):
    
    for i in xrange(0,len(time_to_be_free)):
        if time_to_be_free[i] == 0:
            time_to_be_free[i] += M_ks[i]
            return i
        
    min_time_to_be_free = min(time_to_be_free)
    min_time_to_be_free_index = time_to_be_free.index(min_time_to_be_free)
    
    for i in xrange(0,len(time_to_be_free)):
        time_to_be_free[i] -= min_time_to_be_free
    
    time_to_be_free[min_time_to_be_free_index] += M_ks[min_time_to_be_free_index]
    return min_time_to_be_free_index


def lcm(numbers):
    
    m = max(numbers)
    y = m
    
    while True:
        if reduce(lambda x, y: x & y, map(lambda x: m%x == 0, numbers)):
            return m
        else:
            m += y

def get_which_barber(N, M_ks):
    
    time_to_be_free = [0 for x in xrange(len(M_ks))]
    
    allocated_barber = 1
    for i in xrange(1,N+1):
        allocated_barber = allocate(time_to_be_free, M_ks)
        
    return allocated_barber+1



if __name__ == '__main__':
    
   testcases = int(raw_input())
   
   for testcase in xrange(1, testcases+1):

        B, N = raw_input().split()
        B = int(B)
        N = int(N)
        M_ks = map(lambda x: int(x), raw_input().split())
        
        
        lcm_of_M_ks = lcm_by_gcd(M_ks)
        number_of_people_completed_at_lcm = reduce(lambda x,y: x+y, map(lambda x: lcm_of_M_ks/x, M_ks))
        N = (N-1)%number_of_people_completed_at_lcm + 1
        
        
        print 'Case #'+ str(testcase) + ': ' + str(get_which_barber(N, M_ks))