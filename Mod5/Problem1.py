#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
sum = 0
i = 1

n = int(input("enter a positive number: "))
while n <= 0:
    n = int(input("enter a positive number: "))
while i <= n:
    sum+= i
    i+= 1
print("final sum is",sum)
