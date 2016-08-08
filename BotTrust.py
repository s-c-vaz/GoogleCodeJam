'''
Created on 05-Feb-2016

@author: annervaz
'''

import math

def compute_time(sequence,os_position,bs_position,o_target_index,b_target_index,clock):
    
    
    while o_target_index < len(sequence) or b_target_index < len(sequence):
        
       while o_target_index < len(sequence) and sequence[o_target_index][0] != 'O':
           o_target_index += 1
       while b_target_index < len(sequence) and sequence[b_target_index][0] != 'B':
           b_target_index += 1
           
       #print os_position,bs_position,o_target_index,b_target_index,clock
    
       if o_target_index >= len(sequence) and b_target_index >= len(sequence):
           return clock
       
       os_old_target = o_target_index
       os_old_position = os_position
       if o_target_index < len(sequence):
           if os_position > sequence[o_target_index][1]:
               os_position -= 1
           elif os_position < sequence[o_target_index][1]:
               os_position += 1
           else:
               if b_target_index < o_target_index:
                   pass
               else:
                   o_target_index += 1
                   while o_target_index < len(sequence) and sequence[o_target_index][0] != 'O':
                       o_target_index += 1
       
       if b_target_index < len(sequence):           
           if bs_position > sequence[b_target_index][1]:
               bs_position -= 1
           elif bs_position < sequence[b_target_index][1]:
               bs_position += 1
           else:
               if os_old_target < b_target_index:
                   pass
               else:
                   b_target_index += 1
                   while b_target_index < len(sequence) and sequence[b_target_index][0] != 'B':
                       b_target_index += 1
                       
       clock += 1
    return clock
               

if __name__ == '__main__':

        testcases = int(raw_input())
        for testcase in xrange(0, testcases):
            sequence = raw_input().split()
            sequence = [(sequence[i],int(sequence[i+1])) for i in range(1,len(sequence)-1,2)]
            time = compute_time(sequence,1,1,0,0,0)
            print 'Case #'+ str(testcase+1) + ': ' + str(time)