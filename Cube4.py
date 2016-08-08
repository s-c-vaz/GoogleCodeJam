
def get_neighbouring_positions(position_i, position_j, maze_width):
    
    neighbours = []
    if position_i-1 >= 0:
        neighbours.append((position_i-1,position_j))
    if position_i+1 < maze_width:
        neighbours.append((position_i+1,position_j))
    if position_j-1 >= 0:
        neighbours.append((position_i,position_j-1))
    if position_j+1 < maze_width:
        neighbours.append((position_i,position_j+1))
    
    return neighbours

def check_max_movability(maze, maze_width):
    
    current_number = maze_width * maze_width + 1
    results = []
    continuing_streak = False
    
    number_positions = []
    for i in xrange(maze_width):
        for j in xrange(maze_width):
            number_positions.append((maze[i][j],i,j))
            
    number_positions.sort(key=lambda x:x[0],reverse=True)
    
    while current_number > 1:
        
        if not continuing_streak:
            streak = 1
            current_number -= 1
            results.append((-1*current_number,streak))
            
        current_number_position_i = number_positions[(maze_width*maze_width)-current_number][1]
        current_number_position_j = number_positions[(maze_width*maze_width)-current_number][2]
        
        neighbours = get_neighbouring_positions(current_number_position_i, current_number_position_j, maze_width)
        for id, (neighbour_i,neighbour_j) in enumerate(neighbours):
            if maze[neighbour_i][neighbour_j] == current_number-1:
                current_number = maze[neighbour_i][neighbour_j]
                streak += 1
                results.append((-1*current_number,streak))
                continuing_streak = True
                break
            elif id == len(neighbours)-1:
                continuing_streak = False
                
    results.sort(key=lambda x:(x[1],x[0]), reverse=True)

    return str(results[0][0]*-1) + ' ' + str(results[0][1]) 


if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        maze = []
        maze_width = int(raw_input())
        for i in xrange(maze_width):
            maze.append(map(lambda x: int(x), raw_input().split()))
        
        print 'Case #'+ str(testcase) + ': ' + str(check_max_movability(maze,maze_width)) 