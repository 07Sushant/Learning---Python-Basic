# create a function using following conditions 
# It should accept employee name and salary and display both 
# If the salary is missing in the function the assign default value 10000 to slary 
# Ben(9000) mike(15000) Bob()
a = input("Enter your name: ")
def office(EmployeeName,Salary=10000):
    print(EmployeeName,Salary)
office(a,9000)
office(a,15000)
office(a)