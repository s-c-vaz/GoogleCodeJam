import copy
from SimpleProblems import longest_increasing_subsequence

def get_longest_increasing_subsequences(current_sequence):
    
    length_of_longest_increasing_subsequence_ending_at = [1 for i in xrange(0,len(current_sequence))]
    longest_increasing_subsequence_ending_at = [ [[(i,current_sequence[i])]] for i in xrange(0,len(current_sequence))]
    
    for i in xrange(len(current_sequence)):
        for j in xrange(0,i):
            if current_sequence[j] < current_sequence[i]:
                if length_of_longest_increasing_subsequence_ending_at[j]+1 > length_of_longest_increasing_subsequence_ending_at[i]:
                    length_of_longest_increasing_subsequence_ending_at[i] = length_of_longest_increasing_subsequence_ending_at[j]+1
                    longest_increasing_subsequence_ending_at[i] = [ [] for y in xrange(len(longest_increasing_subsequence_ending_at[j]))]
                    for y in xrange(len(longest_increasing_subsequence_ending_at[j])):
                        longest_increasing_subsequence_ending_at[i][y] = copy.deepcopy(longest_increasing_subsequence_ending_at[j][y])
                        longest_increasing_subsequence_ending_at[i][y].append((i,current_sequence[i]))
                elif length_of_longest_increasing_subsequence_ending_at[j]+1 == length_of_longest_increasing_subsequence_ending_at[i]:
                    
                    z=len(longest_increasing_subsequence_ending_at[i])
                    temp = [ [] for y in xrange(len(longest_increasing_subsequence_ending_at[j]))]
                    longest_increasing_subsequence_ending_at[i].extend(temp)
                    for y in xrange(len(longest_increasing_subsequence_ending_at[j])):
                        longest_increasing_subsequence_ending_at[i][z+y] = copy.deepcopy(longest_increasing_subsequence_ending_at[j][y])
                        longest_increasing_subsequence_ending_at[i][z+y].append((i,current_sequence[i]))

                    
    longest_increasing_subsequence_length = max(length_of_longest_increasing_subsequence_ending_at)
    results = []
    
    for i in xrange(len(current_sequence)):
        if length_of_longest_increasing_subsequence_ending_at[i] == longest_increasing_subsequence_length:
            for j in xrange(0,len(longest_increasing_subsequence_ending_at[i])):
                results.append(longest_increasing_subsequence_ending_at[i][j])
            
    return results
                

def get_minimum_inversion_sequence(item_sequence, initial_guesses):
    
    longest_increasing_subsequences = get_longest_increasing_subsequences(initial_guesses)
    
    results = []
    for longest_increasing_subsequence in longest_increasing_subsequences:
        indices = map(lambda x: x[0],longest_increasing_subsequence)
        excluded_set = [item_sequence[i] for i in xrange(len(item_sequence)) if i not in indices]
        excluded_set.sort()
        results.append(' '.join(excluded_set))
        
    results.sort()
    return results[0]
        
                            
if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        item_sequence = raw_input().split()
        initial_guesses = raw_input().split()
        initial_guesses = map(lambda x: int(x), initial_guesses)
        
        print 'Case #'+ str(testcase) + ': ' + get_minimum_inversion_sequence(item_sequence, initial_guesses)
                
