age = 18
#age = 17 => You aren't old enough!

country = "USA"
#country = "UK" => Yes, i can serve you.
#country = "USA" => Where are you?
#country = "usa" => Where are you?

if age > 17 and country.lower() == "uk":
    print("Yes, i can serve you.")
elif age > 17 and country.lower() != "uk":
    print("Where are you?")    
else:
    print("You aren't old enough!")