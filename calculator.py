#Taking a Input by user.
x = int(input("Enter Your First Number: "))
y = int(input("Enter Your Second Number: "))

#Taking an operators
operator= input("Enter Your operator, [+, -, *, /, %, **, //]: ")

#if and elif condition.

#For Adding Two Numbers.
if operator=="+" :
    print(x+y)

#For subtracting Two Number.
elif operator=="-":
    print(x-y)

#For multiplication of two Number.
elif operator=="*":
    print(x*y)

#For Divide Two Numbers.
elif operator=="/":
    print(x/y)

#For Getting a reminder Value.
elif operator=="%":
    print(x%y)

#For find an exponential form.
elif operator=="**":
    print(x**y)

#For getting a Quotient Value Without any decimal point.
elif operator=="//":
    print(x//y)

#For Invalid input
else:
    print("Invalid Number...")