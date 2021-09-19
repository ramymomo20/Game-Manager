import random

#*------------------------------------------------------------------------------------------------------------------

def rockPaperScissors():
    while True:
        # Choices for the User

        choice = input("Please pick between rock, paper, scissors, or end the game! ")
        options = ["rock", "paper", "scissors"]
        CPUChoice = random.choice(options)
        # Code for the Game and User Inputs
        print("\nYou picked " + choice + " and the computer chose " + CPUChoice + '.')
        if choice == "end the game":
            print("You have chose to end the game, bye!")
            break
        if choice == CPUChoice:
            print("What are the odds? Both you and the computer selected " + choice + ". Bummer, it's a tie!")
        elif choice == "rock":
            if CPUChoice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("CPU Chose Paper, which eats rock! You lose...")
        elif choice == "paper":
            if CPUChoice == "rock":
                print("Paper eats rock! You win!")
            else:
                print("CPU Chose Scissors, which rip paper apart! You lose.")
        elif choice == "scissors":
            if CPUChoice == "paper":
                print("Scissors rip paper! You win!")
            else:
                print("CPU Chose rock, which breaks scissors! You lose.")
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again != "yes":
            return None
    print("See you around! Come play again soon!")

#*------------------------------------------------------------------------------------------------------------------
