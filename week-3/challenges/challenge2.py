# Create a variable, then use a loop to generate a random
# number between 1 and 30 six times.
# For each random number generated, check if this number of
# divisible by 7 or not.

# import random

# # Loop to generate 6 random numbers between 1 and 30
# for i in range(6):
#     random_number = random.randint(1, 30)
#     print(f"The randomly generated number is: {random_number}")
    
#     # Check if the number is divisible by 7
#     if (random_number % 7 == 0):
#         print(f"Hurray. {random_number} is divisible by 7.")
#     else:
#         print(f"{random_number} is not divisible by 7.")

from random import randint
 
for x in range (0,6):
    my_random_number = randint(1,30)
    if (my_random_number%7 == 0):
        print(f"My random number {my_random_number} is divisble by 7")
    else:
        print(f"My random number {my_random_number} is not divisble by 7")