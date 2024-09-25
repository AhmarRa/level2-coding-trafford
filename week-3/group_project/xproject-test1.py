# import from random library
from random import randint, choice
import time
import os

# Hero attributes
def create_hero(name, health, ability, special_skill):
    return [
        name,
        health,
        health,   # Store max health for health restoration
        ability,
        special_skill,
        ["Healing Potion", 3],  # Inventory as a list with item and count
        0,  # experience
        []   # Track collected relics
    ]

# Enemy attributes - 5 enemies per world except for the Centre World
def create_enemy(world):
    if world == "North World":
        enemies = [
            ["Frost Giant", 60],
            ["Ice Dragon", 50],
            ["Snow Wolf", 50],
            ["Frozen Ogre", 60],
            ["Blizzard Bear", 60]
        ]
    elif world == "South World":
        enemies = [
            ["Forest Spirit", 60],
            ["Tree Ent", 65],
            ["Poisonous Vine", 55],
            ["Enchanted Boar", 65],
            ["Cursed Dryad", 60]
        ]
    elif world == "East World":
        enemies = [
            ["Fire Phantom", 70],
            ["Lava Beast", 75],
            ["Cinder Wraith", 60],
            ["Flame Scorpion", 70],
            ["Molten Serpent", 75]
        ]
    elif world == "West World":
        enemies = [
            ["Stone Golem", 80],
            ["Earth Elemental", 75],
            ["Rock Serpent", 75],
            ["Ancient Gargoyle", 75],
            ["Crystal Turtle", 80]
        ]
    elif world == "Centre World":
        enemies = [
            ["Dark Sorcerer", 100]  # Only one enemy in Centre World
        ]
    return choice(enemies)  # Randomly select one enemy from the list

# Loot system
def generate_loot(enemy, character):
    loot = []
    relic_won = False  # Track if a relic is won

    if enemy[0] == "Dark Sorcerer":
        loot.append("Legendary Magic Wand")
        loot.append("Healing Potion")
    else:
        loot.append("Healing Potion")

        # Add relics depending on defeated world
        if enemy[0] in ["Frost Giant", "Ice Dragon", "Snow Wolf", "Frozen Ogre", "Blizzard Bear"]:
            character[6].append("Amulet of Light")  # Update relics
            loot.append("You have collected the Amulet of Light!")
            relic_won = True  # Relic won
        elif enemy[0] in ["Forest Spirit", "Tree Ent", "Poisonous Vine", "Enchanted Boar", "Cursed Dryad"]:
            character[6].append("Sword of Destiny")  # Update relics
            loot.append("You have collected the Sword of Destiny!")
            relic_won = True  # Relic won
        elif enemy[0] in ["Fire Phantom", "Lava Beast", "Cinder Wraith", "Flame Scorpion", "Molten Serpent"]:
            character[6].append("Helm of Power")  # Update relics
            loot.append("You have collected the Helm of Power!")
            relic_won = True  # Relic won
        elif enemy[0] in ["Stone Golem", "Earth Elemental", "Rock Serpent", "Ancient Gargoyle", "Crystal Turtle"]:
            character[6].append("Shield of Hope")  # Update relics
            loot.append("You have collected the Shield of Hope!")
            relic_won = True  # Relic won

    # Add 15 health points if a relic is won
    if relic_won:
        character[1] += 15
        if character[1] > character[2]:
            character[1] = character[2]
        loot.append(f"{character[0]} gains 15 health points! Current health: {character[1]}")

    loot.append(f"{randint(5, 15)} Gold")
    return loot

# Attack function
def attack(character, enemy):
    damage = randint(5, 15)
    enemy[1] -= damage
    print(f"{character[0]} attacks {enemy[0]} for {damage} damage!")

# Use special ability
def use_special(character, enemy):
    if character[4] == "Shield slam":
        damage = randint(10, 25)
        enemy[1] -= damage
        print(f"{character[0]} uses Shield slam on {enemy[0]} for {damage} damage!")
        print(f"{enemy[0]} is stunned and can't attack this turn!")
        return True  # Indicate that the enemy is stunned
    elif character[4] == "Magic Blast":
        damage = randint(15, 30)
        enemy[1] -= damage
        print(f"{character[0]} uses Magic Blast on {enemy[0]} for {damage} damage!")
        return False  # Not stunning
    elif character[4] == "Stealth":
        damage = randint(20, 40)
        enemy[1] -= damage
        print(f"{character[0]} uses Stealth on {enemy[0]} for {damage} damage!")
        return False  # Not stunning

# Heal function
def heal(character):
    if character[5][1] > 0:  # Check Healing Potion count
        healing_amount = randint(15, 30)
        character[1] += healing_amount
        character[5][1] -= 1
        print(f"{character[0]} uses a Healing Potion and restores {healing_amount} health!")
        print(f"{character[0]}'s health is now {character[1]}.")
    else:
        print(f"{character[0]} has no Healing Potions left!")

# Show player stats
def show_stats(character):
    print("\nPlayer Stats:")
    print(f"Name: {character[0]}")
    print(f"Health: {character[1]} / {character[2]}")
    print(f"Experience: {character[6]}")
    print("Inventory:")
    print(f"- {character[5][0]}: {character[5][1]}")  # Inventory item and count
    print("Relics Collected:")
    for relic in character[6]:
        print(f"- {relic}")

# Ending function
def end_game():
    print("\n*******************************************************************")
    print("The Kingdom has been saved. Glory to our heroes and the King.")
    print("The Evil Sorcerer has been destroyed for eternity.")
    print("*******************************************************************\n")
    print("Thank you for playing Quest of the Fallen Kingdom!")
    exit()  # End the game

# Simulate a battle
def battle(character, enemy, world):
    final_boss_defeated = False  # Initialize flag
    print(f"A wild {enemy[0]} appears!")
    while character[1] > 0 and enemy[1] > 0:
        action = input(f"{character[0]}, do you want to (attack, use special, heal)? ").strip().lower()

        if action == "attack":
            attack(character, enemy)
        elif action == "use special":
            if use_special(character, enemy):
                print(f"{enemy[0]} loses its turn!")
                continue
        elif action == "heal":
            heal(character)
            continue
        else:
            print("Invalid action. Please choose again.")
            continue

        print(f"{enemy[0]}'s health: {enemy[1]}")

        if enemy[1] <= 0:
            print(f"{enemy[0]} has been defeated!")

            # If final boss is defeated, set the flag
            if enemy[0] == "Dark Sorcerer":
                final_boss_defeated = True  # Set the flag

            loot = generate_loot(enemy, character)
            print("You collected the following loot:")
            for item in loot:
                print(f"- {item}")

            # Add 25 health points after defeating the enemy
            character[1] += 25
            # Ensure health does not exceed maximum
            if character[1] > character[2]:
                character[1] = character[2]

            print(f"{character[0]} restores 25 health points! Current health: {character[1]}")
            character[6] += 10  # Award experience points
            print(f"{character[0]} gains 10 experience points!")

            # Show player stats after defeating the enemy
            show_stats(character)
            break

        enemy_damage = randint(5, 15)
        character[1] -= enemy_damage
        print(f"{enemy[0]} attacks {character[0]} for {enemy_damage} damage!")
        print(f"{character[0]}'s health: {character[1]}")

        if character[1] <= 0:
            print(f"{character[0]} has been defeated!")  # Defeat message
            break

    return final_boss_defeated  # Return the flag indicating if the final boss was defeated

# Explore a world
def explore_world(world):
    print(f"You are exploring the {world} world.")
    if world == "North World":
        print("The North is a land of ice and snow, filled with fearsome beasts.")
    elif world == "South World":
        print("The South is lush and vibrant, teeming with magic.")
    elif world == "East World":
        print("The East is a land of fire and brimstone, where danger lurks.")
    elif world == "West World":
        print("The West is rocky and treacherous, filled with ancient guardians.")
    elif world == "Centre World":
        print("The Centre World is a realm of darkness and shadows.")

# Main game loop
def main():
    print("Welcome to Quest of the Fallen Kingdom!")
    hero_name = input("Enter your hero's name: ")
    hero_health = 100
    hero_ability = "Basic Attack"
    hero_special_skill = choice(["Shield slam", "Magic Blast", "Stealth"])  # Random special skill

    character = create_hero(hero_name, hero_health, hero_ability, hero_special_skill)

    worlds = ["North World", "South World", "East World", "West World", "Centre World"]

    for world in worlds:
        explore_world(world)
        enemy = create_enemy(world)
        final_boss_defeated = battle(character, enemy, world)

        if final_boss_defeated:
            end_game()  # End game if final boss is defeated

    print("You have completed your journey, but the battle continues!")
    show_stats(character)

# Directly call the main function to start the game
main()
