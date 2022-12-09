'''
3. Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found
by adding up the two numbers before it. The first two numbers are 0 and 1.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above
is 13+21 = 34. 

'''

# Break Line
print("\n")
a = 0
b = 1
x = int(input("Enter the range: "))
print(str(a)+" "+str(b), end=" ")
for i in range(x-2):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# Break Line
print("\n")
# Sushhant
