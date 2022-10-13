# Final Project CMSC 140
# Lilia Bodnar & Adam Bruce
# WHRTLUHC

def wordleGame():
    print("Welcome to our Wordle game! Try and find the five letter word before running out of guesses.")
    print("")
    print("Levels: ")
    print("1: Easy (8 guesses)")
    print("2: Medium (6 guesses)")
    print("3: Hard (4 guesses)")
    print("")
    print("Enter the number corresponding with the number of guesses you would like: ")
    guessLevel = input()

    while(int(guessLevel) != 1 and int(guessLevel) != 2 and int(guessLevel) != 3):
        print("That was not a valid level. Please try again: ")
        guessLevel = input()
    if(int(guessLevel) == 1):
        numGuesses = 8
        guessesLeft = 8
    elif(int(guessLevel) == 2):
        numGuesses = 6
        guessesLeft = 6
    else:
        numGuesses = 4
        guessesLeft = 4




