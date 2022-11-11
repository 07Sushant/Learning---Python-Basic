#Company will give bonus base on following citeria
#Time spend in company                            Bonus
#Greater than 10years                              10%
#more than 6 and less than 10                      10%
#print the net amount


Duration = int(input("How long you have been the part of the company: "))
Salary = int(input("Enter your current slary: "))
if Duration>=10:
    print(((10/100)*Salary)+(Salary),  "your Bonus")
elif Duration>6 and Duration<10:
    print(((8/100)*Salary)+(Salary),  "your Bonus")
elif Duration<6:
        print(int(((5/100)*Salary)+(Salary)),  "your Bonus")
else:
    print("No bonus soRRy")

    

