# create a function that will display the how many item in the list have names more than 5 charactrs
def count(list):
    total = 0
    for i in list:
        if len(i)>5:
            total = total+1
        else:
            total=total
    return total
list = ["Atul","Subham","Anurag","Rahul","Dev","roy"]
total = count(list)
print(total)
#Sushant
