#4.  Create a list of integers. Write code that counts how many numbers are positive and how many are negative, then print both counts.
ls = [1, 5, -2, 3, -10, -4]
positive_ls = sum(1 for n in ls if n > 0)
negative_ls = sum(1 for n in ls if n < 0)

print(f"positive:", positive_ls)
print(f"negative:", negative_ls)
