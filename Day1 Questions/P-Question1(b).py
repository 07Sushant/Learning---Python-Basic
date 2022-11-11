# 1. Write a program to print the following number patterns using a loop
# b
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

rows = int(input("Enter the number of rows: "))
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()