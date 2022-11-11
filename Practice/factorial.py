n = int(input("Enter any number: "))


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
    

num = fact(n)
print(num)
