x = int(input("Enter any number: "))
y = int(input("Enter any number: "))
z = int(input("Enter any number: "))
a = int(input("Enter Your Number: "))
def name(x,y,z):
    return lambda a : a + x**y/z
num = name(x,y,z)
print(num(a))