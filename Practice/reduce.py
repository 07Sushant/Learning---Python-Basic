from functools import reduce 
list1=[3,2,8,16,11,34,17]
x = reduce(lambda a,b :a+b,list1)
print(x)
