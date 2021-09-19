from GamePassword import user_name 
import time # function for the loading simulation

user_name() # calls the username function from the GamePassword.py file

#*-------------------------------------------------------------------------------------------
def welcome(): # introduces the user to the console and the options to play
    print("\n\nWelcome to the Game Hub! Have fun with the games below!\n\n")
    print("Here are your options: ")
    print("""
        1. Rock Paper Scissors with the Computer
        2. Guess the Number
        3. Roll the Dice
        4. I Want to Quit
        """)
    time.sleep(2)
    
#*-------------------------------------------------------------------------------------------

#*-------------------------------------------------------------------------------------------
def game_options(): # takes input from the user
    answer = input("\n\nWhat game would you like to play? Input the corresponding number: (1, 2, 3, 4) ")

    if answer == "1": 
        print("\n Accessing Rock Paper Scissors...")
        time.sleep(3)
        
        from rockPaperScissors import rockPaperScissors # takes function from rockPaperScissors.py file
        rockPaperScissors()
        welcome()
        game_options()

    elif answer == "2":
        print("\n Accessing Guess the Number...")
        time.sleep(3)

        from GuessingNumber import Guess_the_Number # takes function from GuessingNumber.py file
        Guess_the_Number()
        welcome()
        game_options()

    elif answer == "3":
        print("\n Accessing Roll the Dice...")
        time.sleep(3)

        from RollTheDice import Roll_the_dice # takes function from RollTheDice.py file
        Roll_the_dice()
        welcome()
        game_options()

    elif answer == "4":
        print("\n Guess you don't want to have fun. Bye!") 
        answer = None
        return 0

    else:
        print("\n This is Not a Valid Choice, Please Try again... \n")
        welcome()
#*-------------------------------------------------------------------------------------------

welcome() # the program starts with this function and moves onto the game options 
game_options()
