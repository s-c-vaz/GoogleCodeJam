'''
Created on 27-May-2018

@author: annervaz

'''

def get_Count(original_alignment,K):

    count = 0

    current_alignment =  list(original_alignment)

    while ('-' in current_alignment):
         i = current_alignment.index('-')
         if (i+K) > len(current_alignment):
             return 'IMPOSSIBLE'
         else:
             count += 1
             for i in range(i,i+K):
                 if current_alignment[i] == '-':
                     current_alignment[i] = '+'
                 else:
                     current_alignment[i] = '-'

    return str(count)

if __name__ == '__main__':

    testcases = int(input())
    for testcase in range(1, testcases+1):
        original_alignment, K = input().split(' ')
        K = int(K)
        print('Case #'+ str(testcase) + ': ' + get_Count(original_alignment,K))
