#5. Write a function called level_up(experience) that takes a player's experience
#points and returns their new level based on these rules:
#* 0-99 XP → Level 1
#* 100-199 XP → Level 2
#* 200+ XP → Level 3

def level_up(experience):
    if experience >= 200:
        return 3
    elif experience >= 100:
        return 2
    else:
        return 1
experience = int(input("how much XP do you have: "))
level = level_up(experience)
print("Your level is:", level)
