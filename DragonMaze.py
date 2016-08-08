possible_moves = [(1,0),(-1,0),(0,1),(0,-1)]
N = 0
M = 0
maze = None
entry_point = None
exit_point = None

def calculate_collectible_power():
    
    visited_map = [[0 for x in xrange(M)] for y in xrange(N)]
    
    queue_dict = {}
    
    if maze[entry_point[0]][entry_point[1]] != -1:
        queue_dict[(entry_point,1)] = maze[entry_point[0]][entry_point[1]]
        
    while len(queue_dict.keys()) > 0:
        
        for position in queue_dict.keys():  
            if position[0][0] == exit_point[0] and position[0][1] == exit_point[1]:
                return queue_dict[position]
            visited_map[position[0][0]][position[0][1]] = 1
        
        new_queue_dict = {}
        for current_position in queue_dict.keys():
            for possible_move in possible_moves:
                move_to = (current_position[0][0]+possible_move[0],current_position[0][1]+possible_move[1])
                if move_to[0] in range(N) and move_to[1] in range(M):
                    if visited_map[move_to[0]][move_to[1]] == 0 and maze[move_to[0]][move_to[1]] != -1:
                        if (move_to,current_position[1]+1) in new_queue_dict.keys():
                            new_queue_dict[(move_to,current_position[1]+1)] = max(new_queue_dict[(move_to,current_position[1]+1)], queue_dict[current_position] + maze[move_to[0]][move_to[1]])
                        else:
                            new_queue_dict[(move_to,current_position[1]+1)] = queue_dict[current_position] + maze[move_to[0]][move_to[1]]
            
        queue_dict = new_queue_dict
      
    return 'Mission Impossible.'

if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        maze = []
        N, M = map(lambda x:int(x), raw_input().split())
        entry_x,entry_y,exit_x,exit_y = map(lambda x:int(x), raw_input().split())
        entry_point = (entry_x,entry_y) 
        exit_point = (exit_x,exit_y)
        for i in xrange(N):
            maze.append(map(lambda x: int(x), raw_input().split()))
            
      
        print 'Case #'+ str(testcase) + ': ' + str(calculate_collectible_power())
