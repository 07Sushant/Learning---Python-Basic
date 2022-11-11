# 2. Write a program to display all prime numbers within a range
# Take the user input for start and end of range.
# Note: A Prime Number is a number that cannot be made by multiplying
# other whole numbers. A prime number is a natural number greater than 1
# that is not a product of two smaller natural numbers
# Examples:
# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together
# to make it.

# Break Line
print("\n")

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
print("Prime numbers between", start, "and", end, "are:")

for i in range(start,end+1) :
    if i > 1:
        for num in range(2,i) :
            if (i%num) == 0 :
                break
        else:
            print(i)
            
# Break Line
print("\n")