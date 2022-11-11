# 5. Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the
# chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Break Line
print("\n")

# Simple Program Heading
print("FIND FACTORIAL OF INTEGER")

# Input From User
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    # If number is less than 0
    print("Factorial of ", num, " Not Allowed!")

elif num == 1:
    # If number is equal to 0 or 1
    print("The factorial of ", num, " is 1")

else:
    # If number is Greater than 1

    # Loop will start (2 to num+1)
    for number in range(2, num+1):
        factorial = factorial*number
        # answer = "{:,.2f}" . format(factorial)
        
    print("The factorial of", num, "is", factorial)

    # Break Line
    print("\n")


