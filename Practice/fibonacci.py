# WAp to print 10 numbers fibonacci series 
a = 0
b = 1
print(str(a)+" "+str(b),end=" ")
for i in range(0,8):
    c = a + b
    print(c,end=" ")
    a = b
    b = c