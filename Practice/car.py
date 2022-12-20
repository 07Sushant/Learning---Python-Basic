class car:
    wheels = 4
    def __init__(self,brand,mil):
        self.brand = brand
        self.mil = mil
car1 = car("BMW",10)
car2 = car("Tesla",8)

car.wheels = 3

print(car1.brand, car1.mil,car1.wheels)
print(car2.brand, car2.mil,car2.wheels)

# Sushant
# Sushant
