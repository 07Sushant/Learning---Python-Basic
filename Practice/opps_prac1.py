class person:
    def __init__(self):
        self.name = "Sushant"
        self.age = 16
    
    def updateName(self):
        self.name = "Prashant"


    def comapreAge(self,other):
        if self.age == other.age:
            return True
        else:
            return False

person1 = person()
person2 = person()

# person2.name = "kumar"
# person1.updatename()

person1.age = 22
if person1.comapreAge(person2):
    print("They are of same age")
else:
    print("They are of different age ")

bar = 24
print("==" * bar)
print("\n")

print(person1.name, person1.age)
print(person2.name, person2.age)


# Sushant







# types of name that changes with object is known as instance
