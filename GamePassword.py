import string
import random
import time

# *This is for the game console, which incorporates the use of creating a password and username before accessing the game console with games. That file requires this prerequisite
# * to create the password over there.*

#*------------------------------------------------------------------------------------------------------------------
def passwordElements(length): 
    
    # defines the elements need for the password, which includes case-sensitive letters, numbers, and symbols.
    lowercaseLetters = string.ascii_lowercase # all the lowercase letters in the alphabet
    uppercaseLetters = string.ascii_uppercase # all the uppercase letters in the alphabet
    numbers = string.digits # all the numbers from 0-9
    symbols = string.punctuation # symbols such as !@#$%^&*()-=+,.<>/?;:'"[{}]\|`~

    # In order to create the password we must combine all of the elements together.
    all = lowercaseLetters + uppercaseLetters + numbers + symbols

    # randomly jumbles together the elements all together
    combined = random.sample(all, length)

    # joins the entire password together and presents it to the user
    password = ''.join(combined)
    return password

#*------------------------------------------------------------------------------------------------------------------

def user_name():
    userPreferredName = input('\nBefore we begin, what is the name you go by? ')
    print("Hello " + userPreferredName + ", welcome to the Game Console. Where all the fun begins! ")


    print ("\nPlease input your login information below: ")

    username = input('What is your username for the game? ')
    print("That username works, moving on...")

    creatingPassword(username)

#*------------------------------------------------------------------------------------------------------------------

def creatingPassword(username):
    print("\nYou need a password in order to access the Game Console. Please follow the steps below to generate one. ")
    length = range(5, 16)
    length = int(input('\nEnter the length of the password (5 - 16) you would like: \n')) # takes input from the user for password length

    while ((length < 5 or length > 16) and (length != (range(5, 16))) and (length != int)):
        print("Sorry, you must pick the length between 5 to 16.")
        length = int(input('\nEnter the length of the password (5 - 16) you would like: \n'))

    password = passwordElements(length)

    time.sleep(2) # Wait 1 seconds to imitate a loading screen
    print("\nWe now recognize a password in the system. Please wait as we authenticate your account... ")
    time.sleep(3) # Wait 3 seconds to imitate a loading screen

    print("\nThis password is set for the Game Console! ")
    print("-> " + password + " <-")

    loginForGame(username, password)

#*------------------------------------------------------------------------------------------------------------------

def loginForGame(username, password):
    answer = input("Is this your password? Yes or No? \n")
    if answer == 'Yes':
        print("\nUsername: " + username)
        print("Password: " + password + "\n")
        print("\nLogin Successful! Please wait as we load in the games...")
        time.sleep(3) # Wait 3 seconds to imitate a loading screen
    elif answer != 'Yes':
        print("There must be some kind of error, please try again by creating a new password. ")

#*------------------------------------------------------------------------------------------------------------------

