#1. Create a list of integers (you get to pick!). Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numbers = [1,2,10,5,6,9]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
print(f"The sum of all even numbers is:", even_sum)
