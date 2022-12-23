enter=int(input("enter: "))
s=0
j=1
for n in range (0,enter):
    if(n<=1):
        next = n
    else:
        next = s+j
        s=j
        j=next
        print(next)

#Sushant
