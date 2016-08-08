import math

def convert_base(number, sourceBase, destinationBase):
    
    value = reduce(lambda x,y: x+y, map(lambda x: int(sourceBase.index(x[1])) * pow(len(sourceBase), len(number)-x[0]-1), enumerate(number)))
     
    alphabets = []
    while value >= len(destinationBase):
        
        alphabets.append(destinationBase[int(value % len(destinationBase))])
        value = math.floor(value/len(destinationBase))
    
    alphabets.append(destinationBase[int(value)])
    alphabets.reverse()
    return ''.join(alphabets)
    

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(0, testcases):
        number, sourceBase, destinationBase = raw_input().split(' ')
        print 'Case #'+ str(testcase+1) + ': ' + convert_base(list(number), list(sourceBase), list(destinationBase))
