'''
Created on 23-Dec-2015

@author: annervaz
'''
import math

def compute_kth_digit(k,l):
    
    if k <= l/2:
        return compute_kth_digit(k,l/2)
    elif k == l/2+1:
        return 0
    else:
        k = k-l/2-1
        return 1 ^ compute_kth_digit(l/2-k+1,l/2)

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        k = int(raw_input())
        l = 0
        while l < k:
            l = 2 * l + 1
        kth_digit = compute_kth_digit(k,l)
        print 'Case #'+ str(testcase) + ': ' + str(kth_digit)