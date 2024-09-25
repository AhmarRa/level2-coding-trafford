# Create a list of 4 favorite films.
# Use a for loop to show each film in the list.
# Create a function called film_check() that checks if the 3rd film
# in the list is Ghostbusters.
# If it is, it should print“yey it’s ghostbusters”.
# Else, it should print“booo, we want ghostbusters” .  

def film_check(film):
    if film == "Ghostbusters":
        print("yey its Ghostbusters")
    else:
        print("boo, we want Ghostbusters")

film_lists = ["Star Wars","The Thing","Ghostbusters","Midnight Run"]

for film in film_lists:
    print(film)
    film_check(film)