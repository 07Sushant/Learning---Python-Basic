#Write a program to calculate the Area of Triangle.
a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))

# calculating
s = (a + b + c) / 2

#Area calculation
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Print the output
print('The area of the triangle is %0.2f' %area)