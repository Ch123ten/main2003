def createBoard(size):
    return [[0 for j in range(size)]for i in range(size)]

def isSafe(chessBoard, row, col):
    size = len(chessBoard)
    for i in range(size):
        if chessBoard[i][col] == 1:
            return False
    for i in range(size):
        if chessBoard[row][i] == 1:
            return False
    i, j = row, col
    while i>=0 and j>=0:
        if chessBoard[i][j] == 1:
            return False
        i-=1
        j-=1
    i, j = row, col
    while i>=0 and j<size:
        if chessBoard[i][j] == 1:
            return False
        i-=1
        j+=1
    i, j = row, col
    while i<size and j>=0:
        if chessBoard[i][j] == 1:
            return False
        i+=1
        j-=1
    i, j = row, col
    while i<size and j<size:
        if chessBoard[i][j] == 1:
            return False
        i+=1
        j+=1
    return True

def placeQueens(chessboard, row):
    size = len(chessboard)
    global solution
    if row>=size:
        solution+=1
        print("Solution : ",solution)
        for i in chessBoard:
            print(i)
        print()
        return True
    for col in range(size):
        if chessboard[row][col]==0 and isSafe(chessboard, row, col):
            chessboard[row][col] = 1
            placeQueens(chessboard, row+1)
            chessboard[row][col] = 0

chessBoard = createBoard(8)

solution = 0

placeQueens(chessBoard, 0)
