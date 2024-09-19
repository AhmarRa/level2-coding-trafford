# Challenge 1

# Create a variable called password.
# Check how many letters are in the password, if there are less
# than 8, print that the password is too short.
# Otherwise print the password.


#password = "CNat10n"
password = "C0deNat10n"

if len(password) < 8:
    print("Password is too short")
else:
    print(f"Your password is {password}")