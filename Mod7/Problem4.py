#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
#* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
#* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
#* Children (0-18): Free.
age = int(input("How old are you: "))
vehicle = input("are you bringing a vehicle y/n: ")

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif age <= 64:
        return 20 if vehicle == "y" else 10
    elif age >= 65:
        return 15 if vehicle == "y" else 5
    
price = ferry_fare(age, vehicle)
print("Your fare is:", price)
