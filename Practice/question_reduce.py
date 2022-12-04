from termcolor import colored

list1 = [34,88,30,22,10,15,18]
x =list(filter(lambda i : i%5==0,list1))
print("\n")
print(colored(x,"white","on_red"))