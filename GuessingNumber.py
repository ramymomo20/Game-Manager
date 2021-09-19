import random

#*------------------------------------------------------------------------------------------------------------------

def Guess_the_Number(): 
    number = random.randint(1,100) # Computer picks a number from 1 - 100
    count = 0

    while number != count:
        user_guess = int(input("Guess a number from 1 to 100: "))
        count += 1

        if user_guess < number:
            print("\nIncorrect! That guess was too low.")

        elif user_guess > number:
            print("\nIncorrect! That guess was too high.")

        else:
            print("\n\tThat guess was correct! The number was " + str(number) + ". It took you " + str(count) + " attempts.")
            return None

#*------------------------------------------------------------------------------------------------------------------