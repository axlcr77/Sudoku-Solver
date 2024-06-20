import numpy as np

from getBoard import Board

M = 9


def solve(game, row, col, num):

    # Check the row for possible matches
    for i in range(9):
        if game[row][i] == num:
            return False

    # Check the column
    for j in range(9):
        if game[j][col] == num:
            return False

    # Check the box
    boxRow = row - (row % 3)
    boxCol = col - (col % 3)
    for x in range(3):
        for y in range(3):
            if game[x + boxRow][y + boxCol] == num:
                return False
    return True


def Sudoku(game, row, col):
    if (row == M - 1 and col == M):
        return True
    # When the col is at the very end, increase the row and reset the col
    if col == M:
        row += 1
        col = 0

    # Recursive call to move along for numbers that don't need to be solved
    # 0 represents a number that needs to be solved
    if game[row][col] > 0:

        # Increase the column so that the game can be solved by rows
        return Sudoku(game, row, col + 1)

    # Start at 1 and then solve for all numbers
    for num in range(1, M + 1):

        # Solve function will handle checking rows, columns, and boxes
        if solve(game, row, col, num):

            # If the solve function finds that a num is a match then this function will change the value directly.
            game[row][col] = num

            # This will check to see if the number that was added is the correct one
            # as well as check to see if the count is at the end.
            if Sudoku(game, row, col + 1):
                return True

        game[row][col] = 0
    return False


def printSolvedGame(game):
    for i in range(M):
        for j in range(M):
            print(game[i][j], end=" ")
        print()


instance = Board("TextFiles/exper.txt")
game = instance.board



if Sudoku(game, 0, 0):
    printSolvedGame(game)
else:
    print("Solution does not exist")
