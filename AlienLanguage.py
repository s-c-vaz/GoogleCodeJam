import re

valid_words = []

def form_words(pattern):
    
    if pattern.count('(') == 0:
        return [''.join(pattern)]
    
    else:
        
        left_bracket_index = pattern.index('(')
        right_bracket_index = pattern.index(')')
        right_list = form_words(pattern[right_bracket_index+1:])
        fixed_word = pattern[0:left_bracket_index]
        full_list = []
        for index in range(left_bracket_index+1, right_bracket_index):
            for right_element in right_list:
                full_list.append(fixed_word+pattern[index]+right_element)
              
        return full_list

def count_possible_words(pattern):
    
        full_word_list = form_words(pattern)
        
        filtered_word_list = []
        
        for element in full_word_list:
            if element in valid_words:
                filtered_word_list.append(element)
                
        return len(filtered_word_list)


if __name__ == '__main__':
    
    L, D, N = map(lambda x: int(x), raw_input().split())
    valid_words = []
    
    for word in xrange(D):
        valid_words.append(raw_input())
   
    for testcase in xrange(1, N+1):

        pattern = raw_input()
        i = 0;
        regex_pattern = []
        in_bracket = False
        
        while i < len(pattern):
            
            if pattern[i] == '(':
                regex_pattern.append('[')
                in_bracket = True
            elif pattern[i] == ')':
                regex_pattern.append(']')
                in_bracket = False
            else:
                regex_pattern.append(pattern[i])
                if in_bracket and pattern[i+1] != ')':
                    regex_pattern.append('|')
                    
            i += 1
            
        p = re.compile(''.join(regex_pattern))
        matching_words = 0
        for i in xrange(len(valid_words)):
            m = p.match(valid_words[i])
            if m != None:
                if (m.span()[1] == len(valid_words[i])) and (m.span()[0] == 0):
                    matching_words += 1
        
        print 'Case #'+ str(testcase) + ': ' + str(matching_words)