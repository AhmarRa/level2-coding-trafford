def multiply_by_nine_fifths (celsius) :
    return celsius * (9/5)

def get_fahrenheit (celsius):
    return multiply_by_nine_fifths(celsius) + 32

print(f"The temperature is {get_fahrenheit (15)}F.")

# Output : The temperature is 59.0 F.

# or could be written as:
#
# celsius = 15
#
# def multiply_by_nine_fifths (celsius) :
#     return celsius * (9/5)
# def get_fahrenheit (celsius):
#     return multiply_by_nine_fifths(celsius) + 32
# print(f"The temperature is {get_fahrenheit (celsius)}F.")

# Output : The temperature is 59.0 F.