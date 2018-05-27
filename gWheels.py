'''
Created on 16-May-2018

@author: annervaz

couldnt get better that n^3logn, large is not completing with that

'''

def check_possibility(P,Q,pedal_gear_teeths,extra_gear_teeths,tire_gear_teeths):
    tire_gear_teeths.sort()

    for a_index in range(0,len(pedal_gear_teeths)):
        a = pedal_gear_teeths[a_index]
        for c_index in range(0,len(extra_gear_teeths)):
            c = extra_gear_teeths[c_index]
            rhs = a * c * Q
            for b_index in range(0,len(extra_gear_teeths)):
                if b_index == c_index:
                    continue
                b = extra_gear_teeths[b_index]
                d_index_start = 0
                d_index_end = len(tire_gear_teeths)-1
                while(d_index_start<=d_index_end):
                    d_index = int((d_index_start+d_index_end)/2)
                    d = tire_gear_teeths[d_index]
                    lhs = P * b * d
                    if lhs == rhs:
                        return 'Yes'
                    elif lhs < rhs:
                        d_index_start = d_index+1
                    elif lhs > rhs:
                        d_index_end = d_index-1

    return 'No'



if __name__ == '__main__':

    testcases = int(input())
    for testcase in range(1, testcases+1):
        input()
        print('Case #'+ str(testcase) + ':')
        N_p,N_e,N_t = map(lambda x: int(x),input().split(' '))
        pedal_gear_teeths = list(map(lambda x: int(x),input().split(' ')))
        extra_gear_teeths = list(map(lambda x: int(x),input().split(' ')))
        tire_gear_teeths = list(map(lambda x: int(x),input().split(' ')))
        M = int(input())
        for query in range(1,M+1):
            P, Q = map(lambda x: int(x),input().split(' '))
            print(check_possibility(P,Q,pedal_gear_teeths,extra_gear_teeths,tire_gear_teeths))
