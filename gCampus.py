'''
Created on 28-Dec-2015

@author: annervaz

answer for both small and large is marked incorrect by judge
'''
paths = None
roads = None

def distance(i,j):
    
    if i == j: return 0
    nodes = paths[i][j]
    if len(nodes) == 0: return float('inf')
    distance = 0
    for x in xrange(0,len(nodes)-1):
        distance += roads[nodes[x]][nodes[x+1]][0]

    return distance

def update_path(i,j,k):
    
    new_path = []
    for node in paths[i][k]:
        new_path.append(node)
    new_path.remove(k)
    for node in paths[k][j]:
        new_path.append(node)
    paths[i][j] = new_path

if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        N, M = map(lambda x: int(x),raw_input().split(' '))
        roads = [[[] for y in xrange(0,N)] for x in xrange(0,N)]
        paths = [[[] for y in xrange(0,N)] for x in xrange(0,N)]
        for i in xrange(0,M):
            U,V,C = map(lambda x: int(x),raw_input().split(' '))
            if len(roads[U][V]) == 0:
                roads[U][V] = [C,i]
                roads[V][U] = [C,i]
                paths[U][V] = [U,V]
                paths[V][U] = [V,U]
            else:
                oldC = roads[U][V][0]
                if oldC > C:
                    roads[U][V] = [C,i]
                    roads[V][U] = [C,i]
                    paths[U][V] = [U,V]
                    paths[V][U] = [V,U]
                elif oldC == C:
                    roads[U][V].append(i)
                    roads[V][U].append(i)
            
        
        for k in xrange(0,N):
            for i in xrange(0,N):
                for j in xrange(0,N):
                    if distance(i,j) > distance(i,k) + distance(k,j):
                        update_path(i,j,k)
          
                        
        under_optimal_roads = [True for x in xrange(0,M)]
        
        for i in xrange(0,N):
            for j in xrange(0,N):
                nodes = paths[i][j]
                for y in xrange(0,len(nodes)-1):
                    for z in xrange(1,len(roads[nodes[y]][nodes[y+1]])):
                        under_optimal_roads[roads[nodes[y]][nodes[y+1]][z]] = False
               
        print 'Case #'+ str(testcase) + ':'
        
        for x in xrange(0,M):
            if under_optimal_roads[x]:
                print x