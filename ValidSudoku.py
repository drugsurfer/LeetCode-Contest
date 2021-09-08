'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
def isValidSudoku(board):
    col = dict()
    row = dict()
    square = dict()
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in row[r] or
                board[r][c] in col[c] or
                board[r][c] in square[(r // 3, c // 3)]):
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            square[(r // 3, c // 3)].add(board[r][c])
    return True