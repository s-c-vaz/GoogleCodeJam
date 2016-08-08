def all_present(list1, list2):
    
    for element in list2:
        if element not in list1:
            return False
        
    return True


def check_valid_sudoku_board(board, subgrid_width):
    
    elements = [x for x in xrange(1,(subgrid_width*subgrid_width)+1)]
    
    for i in xrange(subgrid_width*subgrid_width):
        row_elements = board[i]
        if not all_present(row_elements, elements):
            return 'No'
        
    for j in xrange(subgrid_width*subgrid_width):
        coloumn_elements = []
        for i in xrange(subgrid_width*subgrid_width):
            coloumn_elements.append(board[i][j])
        if not all_present(coloumn_elements, elements):
            return 'No'
        
    for i in xrange(0,subgrid_width*subgrid_width, subgrid_width):
        for j in xrange(0,subgrid_width*subgrid_width, subgrid_width):
            subgrid_elements = []
            for a in xrange(0,subgrid_width):
                for b in xrange(0,subgrid_width):
                    subgrid_elements.append(board[i+a][j+b])
            if not all_present(subgrid_elements, elements):
                return 'No'
        
    return 'Yes'


if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        board = []
        subgrid_width = int(raw_input())
        for i in xrange(subgrid_width*subgrid_width):
            board.append(map(lambda x: int(x), raw_input().split()))
        
        print 'Case #'+ str(testcase) + ': ' + str(check_valid_sudoku_board(board,subgrid_width)) 