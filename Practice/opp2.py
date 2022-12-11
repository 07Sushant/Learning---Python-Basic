from termcolor import colored
class person:
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def printOutput(self):
        print("My name is : ",self.name, "and Roll number is : " ,self.rollnumber)
        pass

person1 = person("Sushant kumar", 'RKOC28A17')
person2 = person("Lakshay Sharma", 'RKOC28A22')


bar = 30
print("\n")
print("==" * bar)

person1.printOutput()
person2.printOutput()

print("\n")
print("==" * bar)


print("Person 1 ID : ",id(person1))
print("Person 2 ID : ",id(person2))
