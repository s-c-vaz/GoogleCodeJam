'''
Created on 28-Jan-2016

@author: annervaz
'''

M=0
N=0

def get_number_of_kids_alive(board):
    
    number_of_kids_alive = 0
    
    for x in range(M):
        for y in range(N):
            if board[x][y] >= 12:
                neighbours = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                filtered_neighbours = filter(lambda x: x[0]>=0 and x[0]<M and x[1]>=0 and x[1]<N and board[x[0]][x[1]] >=12, neighbours)
                if len(filtered_neighbours) > 0:
                    number_of_kids_alive += 1
    
    return number_of_kids_alive

def are_boards_repeated(new_board,boards):
    
    
    for board in boards:
    
        same = True
        for x in range(M):
            for y in range(N):
                if new_board[x][y] != board[x][y]:
                    same = False
                    break
        if same:
            return True
            
    return False

def move_board(board):
    
    new_board = [[0 for _ in range(N)] for _ in range(M)]
    
    for i in range(M):
        for j in range(N):
            new_board[i][j] = board[i][j]
            
    
    for i in range(M):
        for j in range(N):
            if board[i][j] < 12:
                continue
            neighbours = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            filtered_neighbours = filter(lambda x: x[0]>=0 and x[0]<M and x[1]>=0 and x[1]<N and board[x[0]][x[1]] >=12, neighbours)
            if len(filtered_neighbours) == 0:
                new_board[i][j] = 0
            else:
                new_board[i][j] -= 12
                share = 12/len(filtered_neighbours)
                for x in filtered_neighbours:
                    new_board[x[0]][x[1]] += share
                
    return new_board
            
def get_move_count(boards):
    
    #print move_count,board
    
    board=boards[len(boards)-1]
    number_of_kids_alive = get_number_of_kids_alive(board)
    
    if  number_of_kids_alive == 0:
        return ['F',len(boards)-1]
    
    new_board = move_board(board)
    if are_boards_repeated(new_board,boards):
        return ['I', number_of_kids_alive]
    
    boards.append(new_board)
    return get_move_count(boards)

if __name__ == '__main__':
    
    import sys
    sys.setrecursionlimit(10000)
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):
        M = int(raw_input())
        N = int(raw_input())
        board = []
        for row in xrange(0,M):
            board.append(map(lambda x:int(x), raw_input().split()))
            
        boards = []
        boards.append(board)
        result = get_move_count(boards)
        
        if result[0] == 'F':
            print 'Case #'+ str(testcase) + ': ' + str(result[1]) + ' turns'
        else:
            print 'Case #'+ str(testcase) + ': ' + str(result[1]) + ' children will play forever'
            