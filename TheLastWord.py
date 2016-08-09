'''
Created on 09-Aug-2016

@author: annervaz
'''

if __name__ == '__main__':
    
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        letters = list(raw_input())
        final_string = []
        for i in range(0,len(letters)):
            if len(final_string) == 0:
                new_final_string = [letters[i]]
            for j in range(0,len(final_string)):
                if final_string[j] == letters[i]:
                    if j == len(final_string)-1:
                        new_final_string = [letters[i]] + final_string
                        break
                    continue
                elif final_string[j] < letters[i]:
                    new_final_string = [letters[i]] + final_string
                    break
                else:
                    new_final_string = final_string + [letters[i]]
                    break
            final_string = new_final_string
        print 'Case #'+ str(testcase) + ': ' + ''.join(final_string)