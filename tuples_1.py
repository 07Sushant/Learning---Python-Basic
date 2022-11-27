from termcolor import colored


# tuple1 = ("cars","bike","boat","cycle")
# (item1, *item2, item3) = tuple1
# print(item1,*item2,item3)


# WAP a program to unpack following tuple into 4 variavle 
# tuple = (10,20,30,40)

# tuple1 = (10,20,30,40)
# for i in tuple1:
#     print(i)


# tuple1 = (10,20,30,40)
# (item1, item2, item3, item4)=tuple1
# print(item1,item2,item3,item4)

# tuple1 = (10,20,30,40)
# i = 0
# while i < len(tuple1):
#     print(tuple1[i])
#     i+=1


# tuple1 = (10,20,30,40)
# x = (tuple1[1:3])
# tuple(x)
# print(colored(x,"white","on_red"))

# tuple1 = (10,20,30,40,20,20)
# print(colored(tuple1.count(20),"white","on_red"))
a = input("Enter Name 1: ")
b = input("Enter Name 2: ")
c = input("Enter Name 3: ")
d = input("Enter Name 4: ")
X = (a,b,c,d)
print("\n")
print(colored(X,"white","on_red"))