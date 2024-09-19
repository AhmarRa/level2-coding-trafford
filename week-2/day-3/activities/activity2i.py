age = 18
#age = 17 => You aren't old enough!

country = "USA"

if age > 17 and country == "UK":
    print("Yes, i can serve you.")
elif age > 17 and country != "UK":
    print("Where are you?")    
else:
    print("You aren't old enough!")