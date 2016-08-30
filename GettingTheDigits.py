'''
Created on 30-Aug-2016

@author: annervaz
'''
unique_letters = {0:'z', 2:'w', 4:'u', 6:'x', 8:'g', 1:'o', 3:'t', 5:'f', 7:'s', 9:'i'}
other_letters = {0:['e','r','o'], 2:['t','o'], 4:['f','o','r'], 6:['s','i'], 8:['e','i','h','t'],
                     1:['n','e'],3:['h','r','e','e'],5:['i','v','e'],7:['e','v','e','n'],9:['n','n','e']}



def get_number(number_string):
    
    digits = []
    for i in [0,2,4,6,8,1,3,5,7,9]:
        while unique_letters[i] in number_string:
            digits.append(i)
            number_string.remove(unique_letters[i])
            for letter in other_letters[i]:
                number_string.remove(letter)
    digits.sort()
    digits = map(lambda x: str(x), digits)
    return ''.join(digits)

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        number_string = list(raw_input().lower())   
        print 'Case #'+ str(testcase) + ': ' + get_number(number_string)