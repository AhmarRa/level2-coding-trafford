# import from random library
from random import randint

# Hero attributes
def create_hero(name, health, ability, special_skill):
    return {
        "name": name,
        "health": health,
        "max_health": health,   # Store max health for health restoration
        "ability": ability,
        "special_skill": special_skill,
        "inventory": {"Healing Potion": 3},
        "experience": 0,
        "relics": []            # Track collected relics
    }

# Enemy attributes
def create_enemy(world):
    if world == "North World":
        return {"name": "Frost Giant", "health": 60}
    elif world == "South World":
        return {"name": "Forest Spirit", "health": 70}
    elif world == "East World":
        return {"name": "Fire Phantom", "health": 80}
    elif world == "West World":
        return {"name": "Stone Golem", "health": 90}
    elif world == "Centre World":
        return {"name": "Dark Sorcerer", "health": 100}

# Loot system
def generate_loot(enemy, character):
    loot = []
    if enemy["name"] == "Dark Sorcerer":
        loot.append("Legendary Magic Wand")
        loot.append("Healing Potion")
    else:
        loot.append("Healing Potion")

        # Add relics depending on defeated world
        if enemy["name"] == "Frost Giant":
            character["relics"].append("Amulet of Light")
            loot.append("You have collected the Amulet of Light!")
        elif enemy["name"] == "Forest Spirit":
            character["relics"].append("Sword of Destiny")
            loot.append("You have collected the Sword of Destiny!")
        elif enemy["name"] == "Fire Phantom":
            character["relics"].append("Helm of Power")
            loot.append("You have collected the Helm of Power!")
        elif enemy["name"] == "Stone Golem":
            character["relics"].append("Shield of Hope")
            loot.append("You have collected the Shield of Hope!")

    loot.append(f"{randint(5, 15)} Gold")
    return loot

# Attack function
def attack(character, enemy):
    damage = randint(5, 15)
    enemy["health"] -= damage
    print(f"{character['name']} attacks {enemy['name']} for {damage} damage!")

# Use special ability
def use_special(character, enemy):
    if character["special_skill"] == "Shield slam":
        damage = randint(10, 25)
        enemy["health"] -= damage
        print(f"{character['name']} uses Shield slam on {enemy['name']} for {damage} damage!")
        print(f"{enemy['name']} is stunned and can't attack this turn!")
        return True  # Indicate that the enemy is stunned
    elif character["special_skill"] == "Magic Blast":
        damage = randint(15, 30)
        enemy["health"] -= damage
        print(f"{character['name']} uses Magic Blast on {enemy['name']} for {damage} damage!")
        return False  # Not stunning
    elif character["special_skill"] == "Stealth":
        damage = randint(20, 40)
        enemy["health"] -= damage
        print(f"{character['name']} uses Stealth on {enemy['name']} for {damage} damage!")
        return False  # Not stunning

# Heal function
def heal(character):
    if character["inventory"]["Healing Potion"] > 0:
        healing_amount = randint(15, 30)
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
    print("Relics Collected:")
    for relic in character["relics"]:
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
            
            if enemy["name"] == "Dark Sorcerer":  # Check if final boss is defeated
                end_game()  # Call the end game function
            
            loot = generate_loot(enemy, character)
            print("You collected the following loot:")
            for item in loot:
                print(f"- {item}")

            # Add 25 health points after defeating the enemy
            character["health"] += 25
            # Ensure health does not exceed maximum
            if character["health"] > character["max_health"]:
                character["health"] = character["max_health"]

            print(f"{character['name']} restores 25 health points! Current health: {character['health']}")
            character["experience"] += 10  # Award experience points
            print(f"{character['name']} gains 10 experience points!")

            # Show player stats after defeating the enemy
            show_stats(character)
            break

        enemy_damage = randint(5, 15)
        character["health"] -= enemy_damage
        print(f"{enemy['name']} attacks {character['name']} for {enemy_damage} damage!")
        print(f"{character['name']}'s health: {character['health']}")

        if character["health"] <= 0:
            print(f"{character['name']} has been defeated!")  # Defeat message
            break

# Explore a world
def explore_world(world):
    print(f"You are exploring the {world} world.")
    if world == "North World":
        print("The North is filled with towering mountains and fierce creatures.")
    elif world == "South World":
        print("The South is a lush forest, home to many magical beings.")
    elif world == "East World":
        print("The East is a desolate wasteland, haunted by shadows of the past.")
    elif world == "West World":
        print("The West has ancient ruins, filled with lost treasures and dangers.")
    elif world == "Centre World":
        print("The Centre is where the Evil Sorcerer resides and is where the final battle awaits.")

# Function to select a character
def select_character():
    print("Choose your character:")
    print("1. Eric the Knight - Health: 120, Ability: Sword master, Special Skill: Shield slam")
    print("2. Eli the Elven Mage - Health: 80, Ability: Powerful magic, Special Skill: Magic Blast")
    print("3. Kye the Rogue - Health: 100, Ability: High agility, Special Skill: Stealth")

    while True:
        choice = input("Enter the number of your character (1-3): ")
        if choice == '1':
            return create_hero("Eric the Knight", 120, "Sword master", "Shield slam")
        elif choice == '2':
            return create_hero("Eli the Elven Mage", 80, "Powerful magic", "Magic Blast")
        elif choice == '3':
            return create_hero("Kye the Rogue", 100, "High agility", "Stealth")
        else:
            print("Invalid choice. Please try again.")

# Main game loop
def main_game():
    current_character = select_character()  # Allow player to choose character

    print(f"You are playing as {current_character['name']}.")

    completed_worlds = []  # Track completed worlds

    while True:
        print("\nChoose a world to explore: North, South, East, or West, or type 'exit' to quit.")
        print("Centre will only be unlocked after you've completed all others.\n")
        choice = input("Your choice: ").strip().lower()
        
        # Map short input to full world names
        world_map = {
            'north': 'North World',
            'south': 'South World',
            'east': 'East World',
            'west': 'West World',
            'centre': 'Centre World'
        }

        if choice in world_map:
            world = world_map[choice]
            if world not in completed_worlds:  # Allow exploring only if not completed
                explore_world(world)
                enemy = create_enemy(world)
                battle(current_character, enemy)

                if current_character["health"] > 0:  # Only add to completed if not defeated
                    completed_worlds.append(world)

                # Unlock Centre World after completing all others
                if len(completed_worlds) == 4 and "Centre World" not in completed_worlds:
                    print("You have unlocked the Centre World! Face the Dark Sorcerer!")
            else:
                print(f"You have already completed the {world}!")

        elif choice == 'exit':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def intro():
    print("")
    print("\n*******************************************************************")
    print("Welcome to Quest of the Fallen Kingdom")
    print("\n*******************************************************************")
    print("Oh heroes of the Kingdom of Gdom, you have been summoned by the King.")
    print("Your quest is to defeat the Evil Sorcerer who threatens our way of life.")
    print("You must go to the North World and recover the Amulet of Light.")
    print("You must go to the South World and recover the Sword of Destiny.")
    print("You must go to the East World and recover the Shield of Hope.")
    print("And you must go to the West World and recover the Helm of Power.")
    print("Only then should you proceed to the Centre World where you must face the Evil Sorcerer.")
    print("And only with these powerful relics will you have the necessary tools that can defeat Evil.")
    print("Our fate rests in your hands. Do not fail us.")
    print("********************************************************************\n")
    print("")


# Start the game
intro()
main_game()