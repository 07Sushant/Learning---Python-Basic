def isEven(i):
    return i%2==0

list1 = [3,2,8,16,11,34,17]

# x = filter(isEven,list1)   #filters is a function that take take argument as a function
# x = filter((lambda i : i%2==0))
# print(list(x))

# x = filter(lambda i : i>15,list1)
# print(list(x))
from functools import reduce
# x =map(lambda i : i*i,list1)
x=reduce(lambda a,b:a+b,list1)
print(x)
