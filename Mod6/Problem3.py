#3. Create a list of strings. Write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
ls = ["dog","cat","moose","lion","penguin"]
filtered_ls = [s for s in ls if len(s) > 3]
print(filtered_ls)
