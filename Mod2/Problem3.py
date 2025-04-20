# Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

import math
a = float(input("enter the length of the first side of a triangle"))
b = float(input("enter the length of the second side of a triangle"))
c = float(input("enter the length of the third side of a triangle"))

s = (a + b + c) /2
area = math.sqrt(s* (s - a)*(s - b)*(s - c))
print(s)
print(f"{area:.3f}")
