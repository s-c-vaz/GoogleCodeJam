def get_largest_tidy_number(N):

    digits  = list(map(lambda x: int(x), str(N)))

    for i in range(len(digits)-1,0,-1):
        if digits[i] < digits[i-1]:
            digits[i-1] -=1
            for j in range(i,len(digits)):
                digits[j] = 9
    return str(int(''.join(map(lambda x: str(x),digits))))

if __name__ == '__main__':

    testcases = int(input())
    for testcase in range(1, testcases+1):
        N = int(input())
        print('Case #'+ str(testcase) + ': ' + get_largest_tidy_number(N))
