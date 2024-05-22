import TextFiles

file = open("TextFiles/easy1.txt","r")
file2 = open("TextFiles/easy2.txt","r")
lines = file.read()
lines2 = file2.read()


# print(lines)
# print(lines2)

def getboard(file):
    arr = [[0] * 9 for _ in range(9)]
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

newarr = getboard("TextFiles/easy1.txt")
print(newarr)

file.close()
file2.close()