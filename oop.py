class Laptop:
    def __init__(self,name,processor):
        self.name = name
        self.processor = processor

    def printOutput(self):
        print("My laptop name is : ",self.name, "and the processor is : " ,self.processor)
        pass

laptop1 = Laptop("Asus", 'i7')
laptop2 = Laptop("HP", 'i9')

laptop1.printOutput()
laptop2.printOutput()