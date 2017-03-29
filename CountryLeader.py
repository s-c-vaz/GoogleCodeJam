'''
Created on 27-Feb-2017

@author: annervaz
'''

def get_leader(members):
    
    members_with_count = map(lambda x: (x,len(list(set(list(x.replace(' ', '')))))), members)
    
    members_with_count.sort(key=lambda x: (-x[1],x[0]))
                            
    return members_with_count[0][0]



if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        numberOfMembers = int(raw_input())
        members = []
        for i in xrange(0,numberOfMembers):
            members.append(raw_input())
            
        print 'Case #'+ str(testcase) + ': ' + get_leader(members)
