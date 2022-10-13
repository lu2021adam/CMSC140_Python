# Final Project CMSC 140
# Lilia Bodnar & Adam Bruce
# WHRTLUHC

import random as rand

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
<<<<<<< HEAD
    

wordleGame()



=======
    print(numGuesses)

    # import doc from Prof G and generate a random word from there
    # learned how to import a file from https://datagy.io/python-read-text-file/ and https://www.geeksforgeeks.org/reading-writing-text-files-python/
    # Permission was acquired from Professor Gregg on 10092022 via email
    wordleFile = open("wordle.txt","r")
    print(wordleFile)
        #wordleList = wordleFile.readlines()
        #wordleList = [item.rstrip() for item in wordleList]
        #randomWord = wordleList[randint(0,len(wordleList))]
    #randomWord = randomWord.upper()
    #print("DELETE AFTER TEST CASES; random word is ", randomWord)
>>>>>>> 38cf8e59d8bdcba2a79c64876eacd7b6414db9e7
