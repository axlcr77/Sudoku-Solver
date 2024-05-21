import TextFiles

file = open("TextFiles/easy1.txt","r")
file2 = open("TextFiles/easy2.txt","r")
lines = file.readlines()
lines2 = file2.readlines()
file.close()
file2.close()

print(lines)
print(lines2)
