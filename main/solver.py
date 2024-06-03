import numpy as np

from getBoard import Board


def getBoxes(game):
    boxes = []
    box1 = game[0:3, 0:3]
    box1f = box1.flatten()

    box2 = game[0:3, 3:6]
    box2f = box2.flatten()

    box3 = game[0:3, 6:9]
    box3f = box3.flatten()

    box4 = game[3:6, 0:3]
    box4f = box4.flatten()

    box5 = game[3:6, 3:6]
    box5f = box5.flatten()

    box6 = game[3:6, 6:9]
    box6f = box6.flatten()

    box7 = game[6:9, 0:3]
    box7f = box7.flatten()

    box8 = game[6:9, 3:6]
    box8f = box8.flatten()

    box9 = game[6:9, 6:9]
    box9f = box9.flatten()

    boxes.append(box1f)
    boxes.append(box2f)
    boxes.append(box3f)
    boxes.append(box4f)
    boxes.append(box5f)
    boxes.append(box6f)
    boxes.append(box7f)
    boxes.append(box8f)
    boxes.append(box9f)
    return boxes



def solve(file):
    instance = Board(file)
    game = instance.board
    solved = False
    boxes = getBoxes(game)

    #TODO: Currently you have the boxes as an array so use that to keep solving the game.
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
        if len(possibleNumsBox) == 1:
            game[row][col] = possibleNumsBox[0]
        else:
            possibleNumsCol = checkColumn(row,game)
            if len(possibleNumsCol) == 1:
                game[row][col] = possibleNumsCol[0]


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
