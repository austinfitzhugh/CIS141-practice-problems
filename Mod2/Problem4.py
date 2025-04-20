# Create a program that prompts the user for their birth year and displays a message that says "You are ___ old". Use an f-string in your solution to this problem.

birthyear = int(input("enter your birth year: "))
currentyear = int(input("please enter the current year: "))

yourage = currentyear - birthyear

print(f"you are {yourage} years old")
