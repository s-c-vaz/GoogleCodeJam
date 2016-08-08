import sys


servers = []
queries = []
min_values = []

def initialialize():
    
    for i in xrange(0,len(queries)):
        min_values.append([-1 for j in xrange(0,len(servers))])


def calculate_switches(query,current_server):
   
    if query == len(queries):
        return 0
    
    if min_values[query][current_server] != -1:
        return min_values[query][current_server]

    if servers[current_server] != queries[query]:
        min_values[query][current_server] = calculate_switches(query+1,current_server)
        return min_values[query][current_server]
    else:
        min_values[query][current_server] = float('inf')
        min_swicthes_after_swicthing = min(map(lambda x:calculate_switches(query,servers.index(x)),servers))
        min_values[query][current_server] = 1 + min_swicthes_after_swicthing
        return min_values[query][current_server]
        
         
if __name__ == '__main__':
    
    
    sys.setrecursionlimit(10000)

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        server_count = int(raw_input())
        servers = []
        for i in xrange(0,server_count):
            servers.append(raw_input())
        queries = []
        query_count = int(raw_input())
        for i in xrange(0,query_count):
            queries.append(raw_input())
        
        min_values = []
        initialialize()
        values = map(lambda x: calculate_switches(0,servers.index(x)),servers)
            
        print 'Case #'+ str(testcase) + ': ' + str(min(values))
