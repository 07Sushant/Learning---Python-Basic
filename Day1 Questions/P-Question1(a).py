# 1. Write a program to print the following number patterns using a loop.
# a)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Break Line
print("\n")

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

    # Break Line
print("\n")
# sushant
