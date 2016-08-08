import math

primes = []
non_primes = []
non_primes_factors = []

def is_prime(number):
    
    if number in primes:
        return True, None
    index_in_non_primes = -1
    try: 
        index_in_non_primes = non_primes.index(number)
    except:
        pass
    if index_in_non_primes != -1:
        return False, non_primes_factors[index_in_non_primes]
    if number == 2:
        return True,None
    if number % 2 == 0:
        non_primes.append(number)
        non_primes_factors.append(2)
        return False,2
    for current in xrange(3, int(math.sqrt(number) + 1), 2):
        if number % current == 0: 
            non_primes.append(number)
            non_primes_factors.append(current)
            return False,current
    primes.append(number)
    return True, None

def get_primes():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1
        
def get_jamcoin(N):
    number = 0
    while number < math.pow(2,N-2):
        number_string = '1'+str(bin(number))[2:].zfill(N-2)+'1'
        is_jamcoin = True
        factors = []
        for base in xrange(2,11):
            number_in_base = int(number_string,base)
            prime_check, factor = is_prime(number_in_base)
            if prime_check:
                is_jamcoin = False
                break
            factors.append(factor)
        if is_jamcoin:
           result = [number_string]
           result.extend(factors)
           yield result
        number += 1
        
def get_primes_below_n(n):
    prime_flag =[True for x in xrange(0,n)]
    prime_flag[0] = False
    for i in xrange(2,int(math.sqrt(n)+1),1):
        for j in xrange(2,n):
            m = i*j
            if m > n:
                break
            prime_flag[m-1] = False
            
    primes = [i+1 for i in xrange(0,n) if prime_flag[i]]
    return primes

if __name__ == '__main__':
            
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        N, J = map(lambda x: int(x), raw_input().split(' '))
        jamcoin_generator = get_jamcoin(N)
        print 'Case #'+ str(testcase) + ': ' 
        for i in xrange(0,J):
            print ' '.join(map(str,next(jamcoin_generator)))
    
    #print len(get_primes_below_n(10000000))
            