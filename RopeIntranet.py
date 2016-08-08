

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        number_of_wires = int(raw_input())
        wires = []
        for j in xrange(number_of_wires):
            wire_height_A, wire_height_B = map(lambda x: int(x),raw_input().split())
            wires.append((wire_height_A, wire_height_B)) 
            
        wires.sort(key=lambda x:x[0])
        intersections = 0
        for j in xrange(len(wires)):
           filered_set = [x for x in wires[j+1:] if x[1] < wires[j][1]]
           intersections += len(filered_set)
        
        print 'Case #'+ str(testcase) + ': ' + str(intersections) 