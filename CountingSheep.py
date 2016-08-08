

if __name__ == '__main__':
    

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        N = int(raw_input())
        if N == 0:
            print 'Case #'+ str(testcase) + ': ' + 'INSOMNIA'
            continue
        seen = [False for x in range(0,10)]
        seen_all = False
        i = 1
        while not seen_all:
          for digit in str(N * i):
            seen[int(digit)] = True
          seen_all =  reduce(lambda x,y: x and y, seen)
          if seen_all:
              print 'Case #'+ str(testcase) + ': ' + str(N*i)
              break
          i = i + 1