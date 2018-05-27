'''
Created on 22-May-2018

@author: annervaz

'''

def get_Count(groups,K):

    ab = {}
    cd = {}

    count = 0

    for a in groups[0]:
        for b in groups[1]:
            x = a^b
            if x in ab.keys():
                ab[x] = ab[x]+1
            else:
                ab[x] = 1

    for c in groups[2]:
        for d in groups[3]:
            x = c^d^K
            if x in cd.keys():
                cd[x] = cd[x]+1
            else:
                cd[x] = 1

    for elem in ab.keys():
        if elem in cd.keys():
            count += (ab[elem]*cd[elem])

    return count


if __name__ == '__main__':

    testcases = int(input())
    for testcase in range(1, testcases+1):
        N, K = map(lambda x: int(x),input().split(' ')[0:2])
        groups = []
        for i in range(0,4):
            groups.append(list(map(lambda x: int(x),input().split(' '))))
        print('Case #'+ str(testcase) + ': ' + str(get_Count(groups,K)))
