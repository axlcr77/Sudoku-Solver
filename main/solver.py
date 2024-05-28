from getBoard import Board


def solve(file):
    instance = Board(file)
    game = instance.board
    solved = False
    while not solved:
        # count is for counting the number of boxes, rows, or columns
        count = 0

        # count updates on its own
        for count in range(9):
            solveByBox(count, game)

        for count in range(9):
            solveByRow(count, game)

        for count in range(9):
            solveByCol(count, 9)

        solvedCheck(solved, game)

    return instance


def solveByBox(index, game):
    pass


def solveByRow(index, game):
    pass


def solveByCol(index, game):
    pass


def solvedCheck(solved, game):
    pass


arr = solve("TextFiles/easy1.txt")
print(arr.board)
