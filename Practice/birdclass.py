
# # a = "Hello"
# # b = [1,2,3,4,5,6]

# # print(len(b))

# # def add(a,b,c = 0):
# #     return a+b+c

# # print(add(1,2))
# # print(add(1,2,3))


# class Rect:
#     def calculateArea(self, length = None, breadth = None):
#         if length != None and breadth != None:
#             return length * breadth
#         elif length != None:
#             return length * length

# rectangle = Rect()
# print(rectangle.calculateArea(2,3))
# print(rectangle.calculateArea(2))


class Bird:
    def category(self):
        print("This is a category of bird")
    
    def fly(self):
        print("I can fly")


class Sparrow(Bird):
    def sizeParameter(self):
        print("i am small in size")
class Crow(Bird):
    pass
class Ostrich(Bird):
    def fly(self):
        print("I cannot fly, sorry")

objBird = Bird()
objSparrow = Sparrow()
objCrow = Crow()
objOstrich = Ostrich()

objBird.category()
objBird.fly()
objCrow.category()
objCrow.fly()
objSparrow.category()
objSparrow.fly()
objOstrich.category()
objOstrich.fly()
# sushant
