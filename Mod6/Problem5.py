#5. Create a list of integers. Use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
ls = [1, 2, 3, 4,]
square = []

i = 0
while i <len(ls):
    square.append(ls[i] ** 2)
    i += 1
    
print(square)
