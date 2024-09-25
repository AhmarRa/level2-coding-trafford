# import random library
from random import randint

# Character attributes
def create_hero(name, health, ability, special_skill):
    return {
        "name": name,
        "health": health,
        "max_health": health,  # Store max health for health restoration
        "ability": ability,
        "special_skill": special_skill,
        "inventory": {"Healing Potion": 2},
        "experience": 0
    }

# Enemy attributes
def create_enemy(world):
    if world == "North":
        return {"name": "Frost Giant", "health": 50}
    elif world == "South":
        return {"name": "Forest Spirit", "health": 60}
    elif world == "East":
        return {"name": "Wraith", "health": 70}
    elif world == "West":
        return {"name": "Stone Golem", "health": 80}
    elif world == "Centre":
        return {"name": "Dark Sorcerer", "health": 100}

# Loot system
def generate_loot(enemy):
    loot = []
    if enemy["name"] == "Dark Sorcerer":
        loot.append("Legendary Magic Wand")
        loot.append("Healing Potion")
    else:
        loot.append("Healing Potion")
    loot.append(f"{random.randint(5, 15)} Gold")
    return loot

# Attack function
def attack(character, enemy):
    damage = random.randint(5, 15)
    enemy["health"] -= damage
    print(f"{character['name']} attacks {enemy['name']} for {damage} damage!")

# Use special ability
def use_special(character, enemy):
    if character["special_skill"] == "Shield Bash":
        damage = random.randint(10, 25)
        enemy["health"] -= damage
        print(f"{character['name']} uses Shield Bash on {enemy['name']} for {damage} damage!")
        print(f"{enemy['name']} is stunned and can't attack this turn!")
        return True  # Indicate that the enemy is stunned
    elif character["special_skill"] == "Arcane Blast":
        damage = random.randint(15, 30)
        enemy["health"] -= damage
        print(f"{character['name']} uses Arcane Blast on {enemy['name']} for {damage} damage!")
        return False  # Not stunning
    elif character["special_skill"] == "Backstab":
        damage = random.randint(20, 40)
        enemy["health"] -= damage
        print(f"{character['name']} uses Backstab on {enemy['name']} for {damage} damage!")
        return False  # Not stunning

# Heal function
def heal(character):
    if character["inventory"]["Healing Potion"] > 0:
        healing_amount = random.randint(15, 30)
        character["health"] += healing_amount
        character["inventory"]["Healing Potion"] -= 1
        print(f"{character['name']} uses a Healing Potion and restores {healing_amount} health!")
        print(f"{character['name']}'s health is now {character['health']}.")
    else:
        print(f"{character['name']} has no Healing Potions left!")

# Show player stats
def show_stats(character):
    print("\nPlayer Stats:")
    print(f"Name: {character['name']}")
    print(f"Health: {character['health']} / {character['max_health']}")
    print(f"Experience: {character['experience']}")
    print("Inventory:")
    for item, count in character["inventory"].items():
        print(f"- {item}: {count}")

# Simulate a battle
def battle(character, enemy):
    print(f"A wild {enemy['name']} appears!")
    while character["health"] > 0 and enemy["health"] > 0:
        action = input(f"{character['name']}, do you want to (attack, use special, heal)? ").strip().lower()

        if action == "attack":
            attack(character, enemy)
        elif action == "use special":
            if use_special(character, enemy):
                print(f"{enemy['name']} loses its turn!")
                continue
        elif action == "heal":
            heal(character)
            continue
        else:
            print("Invalid action. Please choose again.")
            continue

        print(f"{enemy['name']}'s health: {enemy['health']}")

        if enemy["health"] <= 0:
            print(f"{enemy['name']} has been defeated!")
            loot = generate_loot(enemy)
            print("You collected the following loot:")
            for item in loot:
                print(f"- {item}")

            # Add 25 health points after defeating the enemy
            character["health"] += 25
            # Ensure health does not exceed maximum
            if character["health"] > character["max_health"]:
                character["health"] = character["max_health"]

            print(f"{character['name']} restores 50 health points! Current health: {character['health']}")
            character["experience"] += 10  # Award experience points
            print(f"{character['name']} gains 10 experience points!")

            # Show player stats after defeating the enemy
            show_stats(character)
            break

        enemy_damage = random.randint(5, 15)
        character["health"] -= enemy_damage
        print(f"{enemy['name']} attacks {character['name']} for {enemy_damage} damage!")
        print(f"{character['name']}'s health: {character['health']}")

        if character["health"] <= 0:
            print(f"{character['name']} has been defeated!")
            break

# Explore a world
def explore_world(world):
    print(f"You are exploring the {world} world.")
    if world == "North":
        print("The North World is filled with towering mountains and fierce creatures.")
    elif world == "South":
        print("The South World is a lush forest, home to many magical beings.")
    elif world == "East":
        print("The East World is a desolate wasteland, haunted by shadows of the past.")
    elif world == "West":
        print("The West World has ancient ruins, filled with lost treasures and dangers.")
    elif world == "Centre":
        print("The Centre World is the heart of Gdom, where the final battle awaits.")

# Function to select a character
def select_character():
    print("Choose your character:")
    print("1. Eric the Knight - Health: 120, Ability: High defence, Special Skill: Shield Bash")
    print("2. Eli the Elven Mage - Health: 80, Ability: Powerful magic, Special Skill: Arcane Blast")
    print("3. Kye the Rogue - Health: 100, Ability: High agility, Special Skill: Backstab")

    while True:
        choice = input("Enter the number of your character (1-3): ")
        if choice == '1':
            return create_hero("Eric the Knight", 120, "High defence", "Shield Bash")
        elif choice == '2':
            return create_hero("Eli the Elven Mage", 80, "Powerful magic", "Arcane Blast")
        elif choice == '3':
            return create_hero("Kye the Rogue", 100, "High agility", "Backstab")
        else:
            print("Invalid choice. Please try again.")

# Main game loop
def main_game():
    current_character = select_character()  # Allow player to choose character
    completed_worlds = []  # Keep track of completed worlds

    print(f"You are playing as {current_character['name']}.")

    while True:
        print("\nChoose a world to explore: North, South, East, West, Centre, or type 'exit' to quit.")
        choice = input("Your choice: ").capitalize()

        if choice == 'Exit':
            print("Thank you for playing!")
            break

        elif choice in ['North', 'South', 'East', 'West']:
            if choice in completed_worlds:
                print(f"You have already completed {choice} World. Choose a different world.")
            else:
                explore_world(choice)
                enemy = create_enemy(choice)
                battle(current_character, enemy)
                completed_worlds.append(choice)  # Mark world as completed

        elif choice == 'Centre':
            if len(completed_worlds) == 4:
                explore_world(choice)
                enemy = create_enemy(choice)
                battle(current_character, enemy)
                print("Congratulations! You have completed the game!")
                break
            else:
                print("You cannot enter the Centre World until you have completed the North, South, East, and West Worlds.")

        else:
            print("Invalid choice. Please try again.")

def intro():
    print("")
    print("")
    print("Welcome to Quest of the Fallen Kingdom")
    print("")
    print("Oh heroes of the Kingdom of Gdom, you have been summoned by the King.")
    print("Your quest is to the defeat the Evil Scorcer who threatens our way of life.")
    print("Our fate rests in your hands. Do not fail us.")
    print("")
    print("")

# Start the game

intro()
main_game()
