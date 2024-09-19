# Challenge 3

# Create a variable called num.
# If num is divisible by 3 print “fizz”, if it’s divisible by 7 print
# “buzz”, if it’s divisible by both 3 and 7 print “fizz buzz”.
# Otherwise print num.

num = 20

if (num % 3 == 0) and (num % 7 == 0): 
    print("fizz buzz")
elif (num % 3 == 0):
    print("fizz")
elif (num % 7 == 0):
    print("buzz")
else:
    print (f"{num} is not divisible by 3 or 7")