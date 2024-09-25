for x in range(1,4):
    my_choice = int(input("Guess the number between 1 and 10, I am thinking of: "))
    if (my_choice == 7):
        print("correct")
        break
    else:
        choices_left = 3 - x
        print(f'try again, you have {choices_left}')