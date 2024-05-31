from getBoard import Board


def solve(file):
    instance = Board(file)
    game = instance.board
    solved = False
    while not solved:
        # count is for counting the number of boxes, rows, or columns
        for row in range(9):
            for col in range(9):
                solveByBox(row, col, game)
                # solveByRow(row, col, game)
                # solveByCol(row, col, game)

        solved = solvedCheck(solved, game)

    return instance


def solveByBox(row, col, game):
    if game[row][col] == 0:
        possibleNumsRow = checkRow(row,game)
        if len(possibleNumsRow) == 1:
                game[row][col] = possibleNumsRow[0]
        else:
            #Check column
            possibleNumsCol = checkColumn(col, game)
            if len(possibleNumsCol) == 1:
                game[row][col] = possibleNumsCol[0]



def solveByRow(row, col, game):
    if game[row][col] == 0:
        possibleNumsBox = checkBox(row, game)
    pass


def solveByCol(row, col, game):
    pass


def solvedCheck(solved, game):
    solved = True
    if game.__contains__(0):
        solved = False
    return solved


def checkRow(index,game):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = game[index]
    numsToRemove = []
    for num in nums:
        if row.__contains__(num):
            numsToRemove.append(num)
    if len(numsToRemove) == 9:
        return []
    for i in numsToRemove:
        nums.remove(i)
    return nums


def checkColumn(index, game):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    col = game[:, index]
    numsToRemove = []
    for num in nums:
        if col.__contains__(num):
            numsToRemove.append(num)
    if len(numsToRemove) == 9:
        return []
    for i in numsToRemove:
        nums.remove(i)
    return nums


def checkBox(index, game):
    box = game[:index+2, :index+2]
    nums = [1,2,3,4,5,6,7,8,9]
    numsToremove = []
    for num in nums:
        if box.__contains__(num):
            numsToremove.append(num)
    if len(numsToremove) == 9:
        return []
    for i in numsToremove:
        nums.remove(i)
    return nums


arr = solve("TextFiles/testSolvebyBox2.txt")
print(arr.board)
