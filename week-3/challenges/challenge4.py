# Create a loop that asks a user to input a number, then displays the
# multiplication table for that numberup to 12 
# e.g., if I input 1, I should
# see this -> 1x1=1, 1x2=2, 1x3=3,......1x12=12
# Incorporate another loop so the program starts again and ask the user for a new number every time it
# finishes.


number = int(input("Enter any integer number less than 13: "))

while number < 13:
    
    for i in range (1,13):
        product = number * i
        print(f'{number} * {i} = {product}')
    number = int(input("Enter any integer number less than 13: "))

# Challenge 3
# Times Table Generator
 
# times_table = int(input("Please enter the times tables you want to see or 13 and above to exit> "))
# while times_table < 13:    
#     for index in range(1,13):
#         result = index * times_table
#         print(f"{times_table} x {index} = {result}")
#     times_table = int(input("Please enter the times tables you want to see or 13 and above to exit> "))
 