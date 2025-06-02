#2. Write a Python program that allows users to log their hiking trips. The program
#should:
#- Use a while loop to repeatedly ask for a hike name and distance in miles
#- Save each entry to hiking_log.txt (each hike on a new line)
#- When the user presses 0, exit the loop & print the contents of hiking_log.txt

print("Hiking trip logs")
print("enter '0' for hike name to finish the log.\n")

hike_name = ""

with open("hiking_log.txt", "a") as file:
    while hike_name != "0":
        hike_name = input("Enter hike name: ")
        if hike_name != "0":
            distance = input("Enter distance in Miles. ")
            if distance.replace('.', '', 1).isdigit():
                file.write(hike_name + " - " + distance + "miles\n")
            else:
                print("enbter a valid distance number.")
                
print("\n-- Hiking Log --")
with open("hiking_log.txt", "r") as file:
    for line in file:
        print(line.strip())
