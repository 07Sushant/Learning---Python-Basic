# a = "Sushant"
# b = [1,2,3,4,5,6]

# print(len(b))

# def add(a,b,c = 1):
#     return a+b+c

# #method overloading
# print(add(1,2,3))
# print(add(1,2))

class React:
    def calculateArea(self, length, breadth):
        return length*breadth
    def calculateArea(self, length):
        return length * length
rectangle = React()
print(rectangle.calculateArea(2,3))
print(rectangle.calculateArea(2))


