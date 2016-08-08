'''
Created on 01-Apr-2016

@author: annervaz
'''

def get_sale_prices(sequence):
    
    if len(sequence) == 0:
        return []
    
    min_number = sequence[0]
    result = []
    result.append(min_number)
    sequence.remove(min_number)
    sequence.remove((min_number*4)/3)
    
    return result + get_sale_prices(sequence)
    
    

if __name__ == '__main__':
   
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        N = int(raw_input())
        sequence = map(lambda x: int(x),raw_input().split())
        result = get_sale_prices(sequence)
        result.sort()
        
        print 'Case #'+ str(testcase) + ': ' + ' '.join(map(str,result))