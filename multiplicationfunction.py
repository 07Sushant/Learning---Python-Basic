# def mult(num1, num2):
#     sum = num1 * num2
#     return sum
# x = mult(2,5)
# print(x)
# def name(firstname, lastname):
#     print("My name is", firstname, lastname)
# name("Sushant","Kumar")
# def name(*args):
#     print(args)
# name("adi","sushant")

def name(name, *args):
    print(name)
    print(args)
name("Sushant","Kumar","Singh")