
import copy

def get_max_nodes_rooted_at(node, parent, graph):

    children = copy.deepcopy(graph[node])
    if parent != None:
        children.remove(parent)
    
    if len(children) == 0 or len(children) == 1:
        return 1
    
    results = []
    for child in children:
        results.append(get_max_nodes_rooted_at(child, node, graph))
        
    results.sort(reverse=True)
    
    return results[0]+results[1]+1


def min_nodes_to_delete(graph):
    
    results = []
    for node in xrange(len(graph)):
        results.append(get_max_nodes_rooted_at(node, None, graph))
        
    return len(graph) - max(results)
        

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        node_count = int(raw_input())
        graph = [[] for i in xrange(node_count)]
        for i in xrange(node_count-1):
            x, y = raw_input().split()
            x = int(x) 
            y = int(y)
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
            
        print 'Case #'+ str(testcase) + ': ' + str(min_nodes_to_delete(graph))
