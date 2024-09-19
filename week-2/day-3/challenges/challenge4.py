# Challenge 4

# Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is the same
# as the first.
# If it is, return True, otherwise return False.

# word = "CodeNation"
word = "Nation"

if word[0].lower() == word[-1].lower():
    print("True")
else:
    print("False")

# Notes:
# word[0] retrieves character from start of the string
# word[-1] retrieves character from end of the string