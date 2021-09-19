import random

#*------------------------------------------------------------------------------------------------------------------

def Roll_the_dice(): 

    Ran = random.randrange(1, 7) # Determining Dice Values through random.randrange function
    Ran2 = random.randrange(1, 7)
    


    print("Guess a number between 1-12: ")
    A = int(input())

    Fin = Ran + Ran2 # Adds dice values together to get a final value

    print("Rolling Dice....")

    # Basically a series of if statements that print corresponding ascii art of the values that were selected by the random function.

    if (Ran == 1):
        print("  .-------.")
        print(" /   o   /|")
        print("/_______/ |")
        print("|       | |")
        print("|       | / ")
        print("|       |/")
        print("'-------'")

    if (Ran == 2):
            print("  .-------.")
            print(" /   O O  /|")
            print("/ ______/ |")
            print("|       | |")
            print("|       | / ")
            print("|       |/")
            print("'-------'")


    if (Ran == 3):
            print("  .-------.")
            print(" /O  O  O/|")
            print("/_______/ |")
            print("|       | |")
            print("|       | / ")
            print("|       |/")
            print("'-------'")

    if (Ran == 4):
                print("  .-------.")
                print(" /O  O  O/|")
                print("/____O___/ |")
                print("|       | |")
                print("|       | / ")
                print("|       |/")
                print("'-------'")

    if (Ran == 5):
                print("  .--0----.")
                print(" /O  O  O/|")
                print("/____O___/ |")
                print("|       | |")
                print("|       | / ")
                print("|       |/")
                print("'-------'")

    if (Ran == 6):
                print("  .------.")
                print(" /O  O  O/|")
                print("/_0__O_0_/ |")
                print("|       | |")
                print("|       | / ")
                print("|       |/")
                print("'-------'")

    if (Ran2 == 1):
        print("  .-------.")
        print(" /   o   /|")
        print("/_______/ |")
        print("|       | |")
        print("|       | / ")
        print("|       |/")
        print("'-------'")
    if (Ran2 == 2):
            print("  .-------.")
            print(" /   O O  /|")
            print("/ ______/ |")
            print("|       | |")
            print("|       | / ")
            print("|       |/")
            print("'-------'")

    if (Ran2 == 3):
            print("  .-------.")
            print(" /O  O  O/|")
            print("/_______/ |")
            print("|       | |")
            print("|       | / ")
            print("|       |/")
            print("'-------'")

    if (Ran2 == 4):
                print("  .-------.")
                print(" /O  O  O/|")
                print("/____O___/ |")
                print("|       | |")
                print("|       | / ")
                print("|       |/")
                print("'-------'")

    if (Ran2 == 5):
                print("  .--0----.")
                print(" /O  O  O/|")
                print("/____O___/ |")
                print("|       | |")
                print("|       | / ")
                print("|       |/")
                print("'-------'")

    if (Ran2 == 6):
                print("  .------.")
                print(" /O  O  O/|")
                print("/_0__O_0_/ |")
                print("|       | |")
                print("|       | / ")
                print("|       |/")
                print("'-------'")


    if (A == Fin):              # Compares what the user guessed to what the random function generated
                                # More specifically it compeares the final values of the Die (Fin) to the guess inputted by the user (A)
        print("You Win!")

    elif(A != Fin):
        print("Better luck next time!") 
        answer = input("Would you like to try again? ")
        if answer == "Yes" or answer == "yes":
            Roll_the_dice()
        elif answer == "No" or answer == "no":
            print("Understood, see you later!")
            return None
        else:
            print("Sorry that input is invalid. Please try again. ")
            answer = input("Would you like to try again? ")

    return None

#*------------------------------------------------------------------------------------------------------------------