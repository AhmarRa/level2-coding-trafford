# Create a while loop to randomly cycle through a list of card suits until a
# given card suit is reached.
# cards = ["Diamond","Spade","Club","Heart"]
# Create a variable called current_card and use a list method to randomly
# give it a value from the list every time the loop runs.
# Then compare this to the suit you want to find to stop the while loop.

import random

cards = ["Diamond","Spade","Club","Heart"]

target_card = "Diamond"
# current_card currently set to nothing.
current_card = ""

while current_card != target_card:  
    current_card = random.choice(cards)
    # uses choice()	from random to return a random element from cards
    print(f'The current card is {current_card}')
    



