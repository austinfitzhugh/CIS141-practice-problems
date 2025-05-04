#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("what is your age: "))
if age > 17:
    print("you can see R rated films")
elif age > 12:
    print("you can see PG-13 rated films")
else:
    print("you can see G rated films")
