board=[
    [8,1,0,0,3,0,0,2,7],
    [0,6,2,0,5,0,0,9,0],
    [0,7,0,0,0,0,0,0,0],
    [0,9,0,6,0,0,1,0,0],
    [1,0,0,0,2,0,0,0,4],
    [0,0,8,0,0,5,0,7,0],
    [0,0,0,0,0,0,0,8,0],
    [0,2,0,0,1,0,7,5,0],
    [3,8,0,0,7,0,0,4,2],
                        ]

def pick_empty(board):
    rows,columns=len(board),len(board[0])
    for r in range(rows):
        for c in range(columns):
            if board[r][c]==0:
                return (r,c)
    #when there is no empty position
    return False

def isValid(board,num,pos):
    row,col=pos
    #checks the row
    for c in range(len(board[0])):
        if c!=col and board[row][c]==num:
            return False

    #checks the column
    for r in range(len(board)):
        if r!=row and board[r][col]==num:
            return False

    #checks the box (3x3)
    rStart=row-row%3
    cStart=col-col%3
    for r in range(rStart,rStart+3):
        for c in range(cStart,cStart+3):
            if r!=row and c!=col and board[r][c]==num:
                return False

    #if there is no dublicate
    return True

def printBoard(board):
    for r in range(len(board)):
        if r%3==0 and r!=0:
            print("- - - - - - - - - - - - ")###
        for c in range(len(board[0])):
            if c%3==0 and c!=0:
                print(" |",end="")
            if c<8:
                print("{:2d}".format(board[r][c]),end="")
            else:
                print("{:2d}".format(board[r][c]))

def sudokuSolver(board):
    #if there is no empty position
    if not pick_empty(board):
        return True
    
    row,col=pick_empty(board)
    for num in range(1,10):
        if isValid(board,num,(row,col)):
            board[row][col]=num
            #continue with the next empty position
            if sudokuSolver(board):
                return True

            board[row][col]=0
    #if there is no possible solution for this position     
    return False

print("The template version:\n")
printBoard(board)
print("\nSolved version of the Sudoku Board!\n")
sudokuSolver(board)
printBoard(board)
