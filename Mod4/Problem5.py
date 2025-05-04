#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping
shipping = 5
total = int(input("please enter your total: "))
if total < 50:
    grand_total = total + shipping
    print("your total cost is",grand_total)
else:
    print("your total cost is",total)
