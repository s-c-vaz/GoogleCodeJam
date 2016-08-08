import math

def convert_base(number, sourceBase, destinationBase):
    
    value = reduce(lambda x,y: x+y, map(lambda x: int(sourceBase.index(x[1])) * pow(len(sourceBase), len(number)-x[0]-1), enumerate(number)))
     
    alphabets = []
    while value >= len(destinationBase):
        
        alphabets.append(destinationBase[int(value % len(destinationBase))])
        value = math.floor(value/len(destinationBase))
    
    alphabets.append(destinationBase[int(value)])
    alphabets.reverse()
    return int(''.join(alphabets))

def get_base_dict(base):
    
    dict = []
    for i in xrange(0,base):
        dict.append(str(i))
        
    return ''.join(dict)
        


def smallest_possible_seconds(number):
    
    symbol_count = 0
    largest_digit = 1
    modified_number = []
    one_used = False
    symbol_values = {}
    
    symbols = [element for element in enumerate(number) if not str.isdigit(element[1])]
    for symbol in symbols:
        if symbol[1] not in symbol_values:
            if symbol[0] == 0:
                symbol_values[symbol[1]] = '1'
                one_used = True
            else:
                if symbol_count == 1 and one_used == True:
                        symbol_count += 1
                symbol_values[symbol[1]] = str(symbol_count)
                symbol_count += 1
    
    print symbol_values
    for element in enumerate(number):
        
        if str.isdigit(element[1]):
            modified_number.append(element[1])
            largest_digit = max(largest_digit,int(element[1]))
        else:
            modified_number.append(symbol_values[element[1]])
            largest_digit = max(largest_digit,int(symbol_values[element[1]]))
    
    seconds = float('inf')
    for base in xrange(largest_digit+1,11):
       result  =  convert_base(modified_number, get_base_dict(base),get_base_dict(10))
       seconds =  min(result, seconds)
       print ''.join(number), ''.join(modified_number), base, result, seconds
       
    return seconds
    

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(0, testcases):
        number = raw_input()
        print 'Case #'+ str(testcase+1) + ': ' + str(smallest_possible_seconds(number))