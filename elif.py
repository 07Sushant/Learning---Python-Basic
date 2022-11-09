#Determining the Grade of student
# #Marks                Grade
# 100-90                  A 
# 90-80                   B 
# 80-70                   c 
# 0-70                    D 

marks = int(input("Enter your obtained marks : "))
if marks > 90 and marks <= 100:
    print("Congratuation your grade is A")
elif marks > 80 and marks <= 90:
    print("Congratuation your grade is B")
elif marks > 70 and marks <= 80:
    print("Congratuation your grade is C")        
else:
    print("Invalid input")