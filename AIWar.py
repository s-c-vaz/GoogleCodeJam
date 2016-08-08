'''
Created on 24-Dec-2015

@author: annervaz

answer for both small and large is marked incorrect by judge
'''

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    
    G=nx.Graph()
    G.add_nodes_from([x for x in xrange(0,P)])
    for node1 in xrange(0,P):
        for node2 in graph[node1]:
            G.add_edge(node1,node2)
          
    nx.draw(G, with_labels=True)
    plt.show()
        

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        P, W = map(lambda x: int(x),raw_input().split(' '))
        wormholes = raw_input().split(' ')
        wormholes = map(lambda x: x.split(','),wormholes)
        wormholes = map(lambda x: (int(x[0]),int(x[1])),wormholes)
        graph = [[] for x in xrange(0,P)]
        for wormhole in wormholes:
            graph[wormhole[0]].append(wormhole[1])
            graph[wormhole[1]].append(wormhole[0])
        
        #draw_graph(graph)
        
        visited = [False for x in xrange(0,len(graph))]
        
        paths = [(0,set(graph[0]),set([0]))]
        visited[0] = True
        
        threatedAI = False
        threatening_paths = []
        if 1 in graph[0]:
            threatedAI = True
            threatening_paths.append(paths[0])
            
        while threatedAI == False:
            
            new_paths = []
            for path in paths:
                current_node = path[0]
                for node in graph[current_node]:
                    if not visited[node]:
                        new_path = (node,path[1].union(set(graph[node])),path[2].union(set([node])))
                        if 1 in graph[node]:
                            threatedAI = True
                            threatening_paths.append(new_path)
                        new_paths.append(new_path)
                for node in graph[current_node]:
                    visited[node] = True
            paths = new_paths
        
        threatening_paths = map(lambda x: (set(x[1]),set(x[2])),  threatening_paths)  
        threatening_paths = map(lambda x: (x[0]-x[1]-set([0]),x[1]-set([0])),  threatening_paths)       
        threatening_paths = map(lambda x: (-1*len(x[0]),len(x[1])), threatening_paths)
        threatening_paths.sort(key=lambda x:(x[1],x[0]))
        
        print 'Case #'+ str(testcase) + ': ' + str(threatening_paths[0][1]) + ' ' + str(-1 * threatening_paths[0][0])
                    
            
            