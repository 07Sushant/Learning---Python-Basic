# WAP a program to display only these number 
# from asyncore import loop
# from a list satisfying following condition 
# Number must be divisible by 5
# if the number is > than 150 then skip 
# if the number is >500 stop the loop



number = [12,75,150,180,145]
for i in number:
    if i<150:
        if i%5==0:
            print(i)
        else:
            continue
    elif i>150 and i<500:
        continue
    else:
        break
