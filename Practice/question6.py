# # create a func in such a way that we can pass any number of arguments to this and it should display each argument's value
# def name(*args):
#     for i in args:
#         print(i)
# name(1,2,3,5,4,6)

def name(firstName="garve", age=100):
    print("My name is  " + firstName, "My age is ", age)
name("Sushant")
name("Kumar",101)