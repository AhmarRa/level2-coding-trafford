# Cash machine time.
# Let’s create one that:

# i) Takes an input of pin number and amount .
# ii) Prints “dispensing cash” if the pin number is correct and there’s enough money to withdraw .
# iii) Displays the new bank balance .

# Be creative!

# The correct pin and current balance
pin = "1234"
balance = 1000

# Function to check if the pin entered is correct
def check_pin(entered_pin):

    # Compare entered pin with correct pin
    if entered_pin == pin:
        print("Pin is correct.")
    else:
        print("Incorrect pin.")

# Function to check if there is enough money to withdraw
def check_balance(amount):

    # Compare requested amount with the current balance
    if amount <= balance:
        print("Sufficient balance.")
    else:
        print("Insufficient balance.")

# Function to process withdrawal
def withdraw_cash(amount):
    # balance set as a global variable
    global balance

    # Subtract the withdrawal amount from the current balance
    balance = balance - amount

# The cash machine function.
def cash_machine():
    # Take pin input
    entered_pin = input("Enter your pin number: ")

    # Check if the pin is correct
    if entered_pin == pin:

        # If the pin is correct, print correct message and ask for the withdrawal amount
        print("Pin is correct.")
        amount = int(input("Enter the amount you want to withdraw: "))

        # Check if there's enough balance
        if amount <= balance:
            print("Dispensing cash...")

            # Update balance
            withdraw_cash(amount)
            print(f'Your new balance is: £{balance}')
        else:
            print("Insufficient balance!")
    else:
        # If the pin is incorrect, print an error message
        print("Incorrect pin!")

# Running the program
cash_machine()