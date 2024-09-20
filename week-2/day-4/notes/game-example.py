import random  # Import the random library to use dice rolls

# Function to roll a die
def roll_dice():
    return random.randint(1, 6)

# Introduction
print("Welcome to the 'Lost in the Forest' adventure!")
print("You find yourself lost in a dark forest, and you must make choices to survive and find your way out.")

# First Decision: Choose a direction
print("\nYou come across a fork in the path.")
print("Do you go left, right, or straight?")

choice1 = input("Enter 'left', 'right', or 'straight': ").lower()

# List of safe choices for an easier check
safe_paths = ['left', 'right', 'straight']

# If choice is not in safe paths, ask again
if choice1 not in safe_paths:
    print("\nInvalid choice! Please choose a valid direction.")
    choice1 = input("Enter 'left', 'right', or 'straight': ").lower()

# Left Path
if choice1 == 'left':
    print("\nYou chose the left path.")
    print("As you walk, you see a wild wolf approaching.")
    
    # Second Decision: How to deal with the wolf
    print("Do you run, climb a tree, or try to scare it away?")
    choice2 = input("Enter 'run', 'climb', or 'scare': ").lower()

    if choice2 == 'run':
        print("\nYou try to run, but let’s see if you can escape by rolling a die.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 4:  # Higher dice rolls let you escape
            print("\nYou ran fast enough to escape the wolf. You made it!")
        else:
            print("\nThe wolf catches you. You didn't make it!")

    elif choice2 == 'climb':
        print("\nYou quickly climb a tree, but let’s see if the tree is tall enough by rolling a die.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 3:  # Higher dice rolls help
            print("\nThe tree was tall enough! The wolf eventually leaves, and you find your way out.")
        else:
            print("\nThe tree wasn't high enough, and the wolf catches you. You didn't make it!")

    elif choice2 == 'scare':
        print("\nYou try to scare the wolf by shouting. Let’s roll a die to see if it works.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice == 6:  # Only the highest roll works
            print("\nAmazingly, your shout worked! The wolf runs away, and you survive.")
        else:
            print("\nYour attempt to scare the wolf fails. You didn't make it!")

    else:
        print("\nInvalid choice! The wolf catches you while you're deciding...")

# Right Path
elif choice1 == 'right':
    print("\nYou chose the right path.")
    print("After walking for a while, you reach a wide river.")

    # Second Decision: How to cross the river
    print("Do you swim across, build a raft, or follow the river downstream?")
    choice2 = input("Enter 'swim', 'raft', or 'follow': ").lower()

    if choice2 == 'swim':
        print("\nYou try to swim across, but let's see if you're strong enough by rolling a die.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 4:
            print("\nYou manage to swim across successfully and continue your journey.")
        else:
            print("\nThe current is too strong, and you didn’t make it!")

    elif choice2 == 'raft':
        print("\nYou build a raft, but let's roll a die to see if it holds together.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 3:
            print("\nYour raft holds together, and you safely cross the river. You find a village on the other side!")
        else:
            print("\nThe raft falls apart, and you didn't make it!")

    elif choice2 == 'follow':
        print("\nYou follow the river downstream, but let’s roll a die to see if you find anything useful.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 2:
            print("\nYou find a bridge, cross it, and escape the forest!")
        else:
            print("\nYou get lost following the river, and night falls. You are stranded!")

# Straight Path
elif choice1 == 'straight':
    print("\nYou chose the straight path.")
    print("As you walk deeper into the forest, the trees get denser, and you can barely see the sky.")

    # Second Decision: What to do next
    print("Do you continue walking, build a shelter, or climb a tree to look around?")
    choice2 = input("Enter 'walk', 'shelter', or 'climb': ").lower()

    if choice2 == 'walk':
        print("\nYou decide to keep walking, but let’s roll a die to see if you avoid dangers.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 5:
            print("\nYou walk safely and eventually find a road. You're saved!")
        else:
            print("\nYou trip and fall into a pit. You didn't make it!")

    elif choice2 == 'shelter':
        print("\nYou build a shelter and wait, but let's see if you're safe by rolling a die.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 3:
            print("\nYour shelter holds up, and a search party eventually finds you. You're rescued!")
        else:
            print("\nYour shelter collapses, and you're exposed to the elements. You didn't make it!")

    elif choice2 == 'climb':
        print("\nYou climb a tree to look around, but let’s roll a die to see if you spot something useful.")
        print("Rolling the die...")
        dice = roll_dice()
        print(f"You rolled a {dice}.")

        if dice >= 4:
            print("\nYou spot a road in the distance. You climb down, head for the road, and you're saved!")
        else:
            print("\nYou can’t see anything useful. You climb down, but get even more lost in the forest.")

# Game End
print("\nThanks for playing the 'Lost in the Forest' adventure!")