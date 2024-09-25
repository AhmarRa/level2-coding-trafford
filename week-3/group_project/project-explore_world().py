# Explore world remains the same
def explore_world(world):
    print(f"You are exploring the {world}.")
    if world == "North World":
        print("The North is filled with towering mountains and fierce creatures.\n")
    elif world == "South World":
        print("The South is a lush forest, home to many magical beings.\n")
    elif world == "East World":
        print("The East is a desolate wasteland, haunted by shadows of the past.\n")
    elif world == "West World":
        print("The West has ancient ruins, filled with lost treasures and dangers.\n")
    elif world == "Centre World":
        print("The Centre is where the Evil Sorcerer resides and is where the final battle awaits.\n")

explore_world("North World")
explore_world("South World")
explore_world("East World")
explore_world("West World")
explore_world("Centre World")