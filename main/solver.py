from getBoard import Board

def solve(file):
    board = Board(file)
    return board

arr = solve("TextFiles/easy1.txt")
print(arr.board)