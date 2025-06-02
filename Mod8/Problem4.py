#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
#by commas. Write a program that reads the poll.txt file
#Count how many votes "yea" or "nay" received and print the results.

with open("poll.txt", "r") as file:
    votes = file.read().strip().lower().split(",")
    
yea_count = votes.count("yea")
nay_count = votes.count("nay")

print("Results:")

print("yea:", yea_count)
print("nay:", nay_count)
