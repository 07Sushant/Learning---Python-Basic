class person:
    def __init__(self,name, age):
        self.__name = name #variable = parameter
        self.__age = age
    
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age
    
person1 = person("ABC", 17)
# print(person1.__name)

print(person1._person__name)