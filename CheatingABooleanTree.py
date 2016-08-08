LEAF = 3
AND = 1
OR = 0
MUTABLE = 1

nodes = []

def min_number_to_achieve(value, node, node_id):
    
    if node[0] == LEAF:
        if node[1] == value:
            return 0
        else:
            return float('inf')
        
    else:
        
        cases = []
        left = ((node_id+1)*2)-1
        right = ((node_id+1)*2)+1-1
        if node[0] == AND:
        
            if value == 1:
                one_on_left = min_number_to_achieve(1, nodes[left],left)
                one_on_right = min_number_to_achieve(1, nodes[right],right)
                cases.append(one_on_left+one_on_right)
                if node[1] == MUTABLE: cases.append(min(one_on_left,one_on_right)+1)
            elif value == 0:
                zero_on_left = min_number_to_achieve(0, nodes[left],left)
                zero_on_right = min_number_to_achieve(0, nodes[right],right)
                cases.append(min(zero_on_left,zero_on_right))
                
        elif node[0] == OR:
            
            if value == 1:
                one_on_left = min_number_to_achieve(1, nodes[left], left)
                one_on_right = min_number_to_achieve(1, nodes[right], right)
                cases.append(min(one_on_left,one_on_right))
            elif value == 0:
                zero_on_left = min_number_to_achieve(0, nodes[left],left)
                zero_on_right = min_number_to_achieve(0, nodes[right],right)
                cases.append(zero_on_left+zero_on_right)
                if node[1] == MUTABLE: cases.append(min(zero_on_left,zero_on_right)+1)
                
        return min(cases)
             
            

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        node_count, root_value = raw_input().split(' ')
        node_count = int(node_count)
        root_value = int(root_value)
        nodes = [0 for x in xrange(0,node_count)]
        node_id = 0
        for node in xrange(0,(node_count-1)/2):
            G, C = raw_input().split(' ')
            G = int(G)
            C = int(C)
            nodes[node_id] = (G,C)
            node_id += 1
        for node in xrange((node_count-1)/2,node_count):
            value = raw_input()
            value = int(value)
            nodes[node_id] = (LEAF,value)
            node_id += 1

        num_changes_required = min_number_to_achieve(root_value, nodes[0],0)
        if num_changes_required == float('inf'):
            print 'Case #'+ str(testcase) + ': ' + 'IMPOSSIBLE'
        else:
            print 'Case #'+ str(testcase) + ': ' + str(int(num_changes_required))