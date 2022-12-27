# Open file 
# open() is method to open file in py

# f = open("demo.txt","a",encoding="utf-8")
# print(f.read())
# print(f.readline())

# f1 = open("demo.txt", "w")
# f1.write("A btech undegrad majoring in computer science\n")
# f1.write("Who love challlenges\n")

# for i in f:
#     f1.write(i)


# try: 
#     f = open("demo.txt")
#     #your codes goes here
# finally:
#     f.close()


# with open("demo.txt") as f:
#     f.read() # example
# your code goes here

f = open("demo.txt", "r")
print(f.read(10))
print(f.tell())
#Sushant




