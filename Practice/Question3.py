#take user input from string if the lemgth of the input is more than three charcter than add "ing" as suffix else print the same
Enter = str(input("Enter your name here: "))
suffix = "ing"
if len(Enter)>3:
    print(Enter+suffix)
else:
    print(Enter)