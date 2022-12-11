# Instance methods
class student:
    numberofsubject = 5
    def __init__(self, mark1, mark2, mark3):
        self.web = mark1
        self.python = mark2
        self.math = mark3
    
    def average(self):
        print((self.web + self.python + self.math)/3)

    # def getMarks(self):
    #     return self.math   #Accessors

    # def setMarks(self,mark):
    #     self.math = mark   #Mutators

    @classmethod
    def classMethodExample(cls):
        return student.numberofsubject
    def staticMethodExample():
        print("this is an example of static method")

student1 = student(5,4,3)
student2 = student(7,8,9)
student3 = student(1,6,9)

print(student.classMethodExample())
student.staticMethodExample()


# student1.average()
# student2.average()
# student3.average()