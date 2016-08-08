import itertools, copy

def apply_permutation(string, permutation):
    
    new_string = copy.deepcopy(string)
    
    for i in xrange(0,len(string),len(permutation)):
        for j in xrange(len(permutation)):
            new_string[i+j] = string[i+permutation[j]]
            
    return new_string
    
def get_length(string):
    
    length = 1
    for i in xrange(0,len(string)-1):
        if string[i] == string[i+1]:
            continue
        else:
            length += 1
            
    return length

def get_minimum_compressed_length(string, k):
    
    minimum_compression_length = float('inf')
    for permutation in itertools.permutations([x for x in xrange(0,k)]):
        minimum_compression_length = min(minimum_compression_length, get_length(apply_permutation(string,permutation)))
    
    return minimum_compression_length
    

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        k = int(raw_input())
        string = list(raw_input())
        
        print 'Case #'+ str(testcase) + ': ' + str(get_minimum_compressed_length(string,k))