def is_ugly_number(number):
    
    if number%2 == 0 or number%3 == 0 or number%5 == 0 or number%7 == 0:
        return True
    
    return False
    
def count_ugly_numbers(digits):
    
    
    counts = [[0 for x in xrange(210)] for y in xrange(len(digits))]
    
    counts[0][int(digits[0])%210] = 1
        
    for i in xrange(1,len(digits)):
        
        for x in xrange(210):
    
                counts[i][(10*x+int(digits[i])) % 210] += counts[i-1][x]
                
                counts[i][(x+int(digits[i])) % 210] += counts[i-1][x]
                
                counts[i][(x-int(digits[i])) % 210] += counts[i-1][x]
            
    count = 0
    for x in xrange(210):
        if is_ugly_number(x):
            count += counts[len(digits)-1][x]
    
    return count
            

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        digits = raw_input()
        print 'Case #'+ str(testcase) + ': ' + str(count_ugly_numbers(digits))
                