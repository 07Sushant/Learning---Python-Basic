# def  count(listofNum):
#     even=0
#     odd=0

#     for i in listofNum:
#         if i % 2 == 0:
#             even += 1
#         else:
#          odd += 1
#     return even,odd

# listofNum=[32,21,64,100,13]
# even, odd = count(listofNum)
# print(even)
# print(odd)

def count(list):
    total = 0
    for i in list:
        if len(i)>5:
            total = total+1
        else:
            total=total
list = ["Atul","Subham","Anurag","Rahul","Dev","roy"]
total = count(list)
print(total)