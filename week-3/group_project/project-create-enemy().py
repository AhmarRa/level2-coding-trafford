from random import choice

# Enemy attributes - 5 enemies per world except for the Centre World
def create_enemy(world):
    if world == "North World":
        enemies = [
            {"name": "Frost Giant", "health": 60},
            {"name": "Ice Dragon", "health": 50},
            {"name": "Snow Wolf", "health": 50},
            {"name": "Frozen Ogre", "health": 60},
            {"name": "Blizzard Bear", "health": 60}
        ]
    elif world == "South World":
        enemies = [
            {"name": "Forest Spirit", "health": 60},
            {"name": "Tree Ent", "health": 65},
            {"name": "Poisonous Vine", "health": 55},
            {"name": "Enchanted Boar", "health": 65},
            {"name": "Cursed Dryad", "health": 60}
        ]
    elif world == "East World":
        enemies = [
            {"name": "Fire Phantom", "health": 70},
            {"name": "Lava Beast", "health": 75},
            {"name": "Cinder Wraith", "health": 60},
            {"name": "Flame Scorpion", "health": 70},
            {"name": "Molten Serpent", "health": 75}
        ]
    elif world == "West World":
        enemies = [
            {"name": "Stone Golem", "health": 80},
            {"name": "Earth Elemental", "health": 75},
            {"name": "Rock Serpent", "health": 75},
            {"name": "Ancient Gargoyle", "health": 75},
            {"name": "Crystal Turtle", "health": 80}
        ]
    elif world == "Centre World":
        enemies = [
            {"name": "Dark Sorcerer", "health": 100}  # Only one enemy in Centre World
        ]
    return choice(enemies)  # Randomly select one enemy from the list

# code below to test output.  
#  
# You can replace "North World" with any world you choose

enemy = create_enemy("North World")
print(enemy)

# selected_world = "North World"  # Change this to test different worlds
# enemy = create_enemy(selected_world)
# print(f"You encounter a {enemy['name']} with {enemy['health']} health!")





