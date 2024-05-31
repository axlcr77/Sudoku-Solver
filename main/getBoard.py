import numpy as np
file = open("TextFiles/easy1.txt","r")
file2 = open("TextFiles/easy2.txt","r")
lines = file.read()
lines2 = file2.read()

class Board:
    def __init__(self, file):
        self.file = file
        self.board = self.getboard(file)

    def getboard(self, file):
        arr = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        
        with open(file, "r") as file2:
            lines = file2.readlines()
            rows = [line.strip() for line in lines]
        row = 0
        col = 0
        for i in range(9):
            currentRow  = rows[i]
            numbers = currentRow.split(" ")
            for number in numbers:
                arr[col][row] = int(number)
                row += 1
            row = 0
            col += 1
        return arr

# newarr = getboard("TextFiles/easy1.txt")

file.close()
file2.close()