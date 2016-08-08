if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        
        first_answer = int(raw_input())
        possible_answers_1 = []
        for i in range(1,5):
           cards = raw_input().split(' ')
           if i == first_answer:
               possible_answers_1 = cards
               
        second_answer = int(raw_input())
        possible_answers_2 = []
        for i in range(1,5):
           cards = raw_input().split(' ')
           if i == second_answer:
               possible_answers_2 = cards
       
        answer = set(possible_answers_1).intersection(set(possible_answers_2))
        
        if len(answer) == 1:
            print 'Case #'+ str(testcase) + ': ' + answer.pop()
        elif len(answer) == 0:
            print 'Case #'+ str(testcase) + ': ' + 'Volunteer cheated!'
        else:
            print 'Case #'+ str(testcase) + ': ' + 'Bad magician!'