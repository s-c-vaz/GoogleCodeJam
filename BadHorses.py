
from Graphs import check_graph_bipartite

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        name_index = []
        graph = {}
        trouble_some_pair = int(raw_input())
        for pair in xrange(0,trouble_some_pair):
            name1, name2 = raw_input().split(' ')
            if name1 in name_index:
                name1_index = name_index.index(name1)
            else:
                name_index.append(name1)
                name1_index = name_index.index(name1)
            if name2 in name_index:
                name2_index = name_index.index(name2)
            else:
                name_index.append(name2)
                name2_index = name_index.index(name2)
            if name1_index not in graph.keys():
                graph[name1_index] = []
            if name2_index not in graph.keys():
                graph[name2_index] = []
            graph[name1_index].append((name1_index,name2_index))
            graph[name2_index].append((name2_index,name1_index))
            
        if check_graph_bipartite(graph):
            print 'Case #'+ str(testcase) + ': ' + 'Yes' 
        else:
            print 'Case #'+ str(testcase) + ': ' + 'No' 
