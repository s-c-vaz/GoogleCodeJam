def get_flips(stack):

    first_blank = stack.find('-')
    if first_blank == -1:
        return 0
    first_happy_after_first_blank = stack.find('+',first_blank+1)
    if first_happy_after_first_blank == -1:
        if first_blank == 0:
            return 1
        else:
            return 2
    else:
        if first_blank == 0:
            return 1+get_flips(stack[first_happy_after_first_blank:])
        else:
            return 2+get_flips(stack[first_happy_after_first_blank:])
         

if __name__ == '__main__':
    

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        stack = raw_input()
        print 'Case #'+ str(testcase) + ': ' + str(get_flips(stack)) 