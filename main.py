"""
This a game called HangMan.
Guess the word letter by letter to win the game.
Go Ahead and try to beat this game......
    Note: This program runs infinite times until you input N or n.
"""

import random
from figures import *  # importing the figures.py which contains kind man figures.


def main():
    def chooseLevel():  # Choose your level to fetch word from suitable list.
        print("Choose One of these levels.")
        print("> Easy \n> Medium \n> Hard")
        level = input("which one? ").strip().lower()
        return level

    def updateGuess(word):  # Alter the chosen char with '#' to avoid redundancy.
        for i in range(len(word)):
            if word[i] == guess:
                update[i] = guess
                word[i] = "#"
        printUpdate()
        print()

    def printUpdate():  # print the list with dashes.
        for i in update:
            print(i, end=" ")

    while True:  # making sure that user choose the correct category.
        Level = chooseLevel()
        if Level in ["easy", "medium", "hard"]:
            break
        else:
            print("That's not a valid category, Try again :(")

    # word lists for each levels.
    easy = ["cloud", "python", "java", "git", "django"]
    medium = ["internet", "unlimited", "programming", "notification", "android"]
    hard = ["awkward", "technophile", "crowdsources", "pneumonia", "jinx"]

    random_word = random.choice(eval(Level))  # Choosing a random word from list.
    word_list = list(random_word)  # converting the random word in to list.
    update = [" _ "] * len(random_word)  # Empty word list
    wrong = 0

    sayHi()
    print(f"Guess the {len(random_word)} letter word to save the Kind man;)")

    while wrong < 5:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Invalid Input, Try again :(")
        else:
            if guess not in word_list:
                wrong += 1
                kindMan(wrong)
                print()
            else:
                updateGuess(word_list)
            if " _ " not in update:
                break

    if " _ " in update:
        print(f"The word is {random_word}.")
        print("GAME OVER, You let the kind man die :(")
    else:
        print()
        print("Whoa...Great job buddy :)\nYou saved him ;)")
        print()
        gratitude()
        return True


# Run infinite times until user inputs 'N' or 'n'.y
win = 0
played = 0
while True:
    start = input("Do you want to dive in to the game? <Y/N> :").strip().lower()
    if start in ['y', 'n']:
        if start == 'y':
            played += 1
            if main():
                win += 1
        else:
            print()
            break
    else:
        print("Invalid, Just Type 'Y' or 'N'")
while True:
    if played == 0:
        summary = ""
        break
    summary = input("Do you want summary of your game record? <Y/N>").strip().lower()
    if summary in ['y', 'n']:
        break
    else:
        print("Invalid entry, please enter 'Y' or 'N' ")

if summary == 'y':
    print("_______S U M M A R Y_______")
    print(f"Game played:  {played}")
    print(f"Solved     :  {win}")
    print("Your win Rate: ", "{:.2f}".format(win/played))

print("TaTa By By...")

