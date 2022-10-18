# Final Project CMSC 140
# Lilia Bodnar & Adam Bruce
# WHRTLUHC

import random as rand

import re as regex

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

    while(int(guessLevel) != 1 and int(guessLevel) != 2 and int(guessLevel) != 3): # add something to make sure it runs if the variable is a letter also
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

# import doc from Prof G and generate a random word from there
    # learned how to import a file from https://datagy.io/python-read-text-file/ and https://www.geeksforgeeks.org/reading-writing-text-files-python/ and https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/
    # Permission was acquired from Professor Gregg on 10092022 via email
    
    # open the file as file, split by whitespace, and select a random word with rand
    with open("wordle.txt", "r") as file:
        words = file.read()
        seperatedWords = list(map(str, words.split()))
        randomWord = rand.choice(seperatedWords)

    print("random word: ", randomWord)

    # 1. write a loop here that runs for the number of guesses the user had to guess the random word
        # 1.2 write an if/else to tell them if they got it right or wrong or to guess again or to say they lost and print out the word
    for i in range(numGuesses): 
        guessesLeft -= 1
        print("Please guess the word: ")
        userGuess = input()
        while(len(userGuess) != 5):
            print("Please guess a 5 letter word: ")
            userGuess = input()
        userGuess = str(userGuess).lower()
        correctLetters = ""
        print("user guess " ,userGuess)

        if userGuess == randomWord:
            print("You won! Thanks for playing :^)")
            break
        else: 
            for letter in range(len(userGuess)):
                if userGuess[letter] == randomWord[letter]:
                    correctLetters += userGuess[letter]
                else:
                    correctLetters += "-"
            print("")
            print("You have: ", guessesLeft, " guesses remaining.")
        print("Your correct placements are: ", correctLetters)
    if(guessesLeft == 0):
        print("")
        print("You didn't guess the word. Please play again. The random word was",randomWord)

def playWordle():
    print("Do you want to play wordle?")
    playAgain = str(input())
    yes_regex = regex.compile(r'(Y|y)(es)?$') # a regex for valid forms of yes
    no_regex = regex.compile(r'(N|n)(o)?$') # A regex for valid forms of no
    while(regex.match(yes_regex, playAgain) or regex.match(no_regex, playAgain)):
        if regex.match(yes_regex, playAgain):
            wordleGame()
            print("Do you want to play again? (yes/no)")
            playAgain = str(input())
        elif regex.match(no_regex, playAgain):
            print("Call the function again when you want to play Wordle!")
    print("Please enter a valid form of yes or no. Valid Forms: Yes, Y, yes, y, No, N, no, n")
    playAgain = str(input())


playWordle()