# Challenge 7

# Create a variable called num.
# Check if the number is a palindrome (looks the same forward
# as it does backwards e.g. 1001 or 20202).

# num = 10201
# num = 1001
num = 12345

string = str(num)

if string[0] == string[-1] and string[1] == string[-2]:
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')