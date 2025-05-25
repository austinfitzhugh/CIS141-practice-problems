#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
#For example, water is very effective to fight fire.
#Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
#strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
#simple type effectiveness rules. Your solution only needs to work for these three sets of input:
#print(type_advantage("Water", "Fire")) # "Super Effective"
#print(type_advantage("Fire", "Water")) # "Not Very Effective"
#print(type_advantage("Electric", "Grass")) # "Neutral"

def type_advantage(attacker, defender):
    if attacker == "water" and defender == "fire":
        return "super effective!"
    elif attacker == "fire" and defender == "water":
        return "not very effective."
    elif attacker == "electric" and defender == "grass":
        return "neutral"
    
print(type_advantage("water", "fire"))
print(type_advantage("fire", "water"))
print(type_advantage("electric", "grass"))
