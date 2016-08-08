
import itertools
import copy

DISPLAY = ['1111011', '1111111', '1110000', '1011111', '1011011', '0110011', '1111001', '1101101', '0110000', '1111110']
states = []
possible_malfunctioning_positions = []


def alter_positions(state, altered_positions, alter_value='1'):
    
    altered_state = copy.deepcopy(list(state))
    for i in range(len(altered_positions)):
        altered_state[altered_positions[i]] = alter_value
        
    return ''.join(altered_state)

def get_possible_actual_states(state):
    
    possible_actual_states = []
    for i in xrange(0,len(possible_malfunctioning_positions)+1):
        
        altering_positions_possibilities = itertools.combinations(possible_malfunctioning_positions, i)
        while True:
            try:
                altered_positions = altering_positions_possibilities.next()
                altered_state = alter_positions(state,altered_positions)
                if altered_state in DISPLAY:
                    possible_actual_states.append((altered_state, altered_positions))
            except StopIteration as e:
                break
            
    return possible_actual_states
        
def get_next_state(state):
    
    for i in range(len(DISPLAY)):
        if DISPLAY[i] == state:
            return DISPLAY[(i+1)%len(DISPLAY)]
        
    return None

        
def get_next_display_pattern(current_index, current_hypothesis, actually_altered_positions):
    
    if current_hypothesis == None:
        answers = []
        for i in range(len(DISPLAY)):
            answer =  get_next_display_pattern(current_index, DISPLAY[i],actually_altered_positions)
            if answer != None:
                answers.append(answer)
        if (len(set(answers)) == 1):
            return answers[0]
        else:
            return None
        
    if current_index == len(states):
        altered_current_hypothesis = alter_positions(current_hypothesis, actually_altered_positions, '0')
        return altered_current_hypothesis
    
    possible_actual_states = get_possible_actual_states(states[current_index])
    index_of_current_hypothesis = -1
    try:
        index_of_current_hypothesis = map(lambda x: x[0],possible_actual_states).index(current_hypothesis)
    except ValueError as e:
        return None

    z = copy.deepcopy(actually_altered_positions)
    z.extend(possible_actual_states[index_of_current_hypothesis][1])
    return get_next_display_pattern(current_index+1, get_next_state(current_hypothesis),z)

if __name__ == '__main__':


    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        states = raw_input().split()
        if len(states) > 1:
            states = states[1:]  
        states = map(lambda x: list(x), states)
        possible_malfunctioning_positions = set([0,1,2,3,4,5,6])
        for state in states:
            indices_of_0 = [x for x in range(len(state)) if state[x] == '0']
            possible_malfunctioning_positions = possible_malfunctioning_positions.intersection(set(indices_of_0))

        result = get_next_display_pattern(0, None, [])
        if result == None:
            result = 'ERROR!'
        print 'Case #'+ str(testcase) + ': ' +  result
        