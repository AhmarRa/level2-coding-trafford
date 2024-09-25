from random import randint
from time import sleep

target_number = 79
generated_number = randint(1,100)
counter = 0
 
while generated_number != target_number:
    #sleep(0.1)
    print(counter,generated_number)
    generated_number = randint(1,100)
    counter += 1
 
print(f"you found the number and it was {generated_number} after {counter} goes")
 