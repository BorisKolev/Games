"""
Hangman
Created: 30/10/2018
Author: Borislav Kolev
"""

from random import randint
from time import sleep


def hangman_game():

    # The words WILL NOT be read from a file instead I have created a dictionary
    # Keys in the dictionary will be the available words and the items will be the hints for the words
    # new keys should be entered only with uppercase

    dictionary = {"MEMORYLEAK": "hint for the word: occurs in programming when the memory allocation is managed "
                                "incorrectly",
                  "BORISLAV": "hint for the word: The name of the creator",
                  "ZLATINA": "hint for the word: A golden nightmare which you can get rid of ",
                  "RUSKO": "hint for the word: Probably the smartest man I have ever met and my closest friend,"
                           " currently studying in Oxford",
                  "PYTHON": "hint for the word: The language in which this program is written",
                  "CONCATINATION": "term used in programming for joining strings",
                  "Michael": "hint for the word: Name of the co-founder of MySQL"
                  }

    # Storing the keys from the dictionary into class 'dict_keys' then turning it into class 'list'
    words = list(dictionary.keys())

    # Just an introduction
    print("### Hello, you just entered a hangman ###\n")
    usr_name = input("Could you please enter your name: ")

    # THIS FUNCTION IS THE MAIN BODY OF THE PROGRAM

    def hangman():

        start = True
        while start:
            user_guessed_letters = ""
            lives = 5
            print("The game is starting")
            sleep(2)
            print("Picking a random word")
            sleep(2)
            print("You start with", lives, "lives \nYou can always write 'quit' during the game in order to quit\n")
            sleep(2)
            # Picking a random word
            rand_word = words[randint(0, len(words) - 1)]
            # Printing the hint
            print(dictionary[rand_word])

            # For every character it will display an underscore
            # This will be printed only the first time
            rand_word_len = len(rand_word) - 1
            while rand_word_len >= 0:
                print("_", end=" ")
                rand_word_len -= 1

            # The game has to finish in order for the while loop to finish
            while lives >= 0:

                usr_choice = input("\n\nEnter a character: ")

                # Checking if the user wants to quit
                if usr_choice.upper() == "QUIT":
                    sleep(2)
                    start = False
                    break

                # Checking if the user input a single letter
                elif len(usr_choice) == 1 and usr_choice.isalpha():
                    usr_choice = usr_choice.upper()

                    # If letter was not in the word
                    if usr_choice not in rand_word:
                        # Take one life
                        lives -= 1
                        if lives == 1:
                            print(usr_name, " lost one life, 1 life left now")
                            print(usr_name, "That will be your last life be careful !!")
                        elif lives > 1:
                            print(usr_name, "lost one life,", lives, " lives left now")
                        # If no more lives are left you lose
                        else:
                            print("Sorry you lost please try again ")
                            start = False
                            break

                        # Printing the underscores with the guessed letters
                        for i in rand_word:
                            if i in user_guessed_letters:
                                print(i, end=" ")
                            else:
                                print("_", end=" ")

                    # If the user guesses a letter
                    else:
                        # Add this letter to the user guessed letter string
                        user_guessed_letters += usr_choice

                        # Printing the underscores with the guessed letters
                        for i in rand_word:
                            if i in user_guessed_letters:
                                print(i, end=" ")
                            else:
                                print("_", end=" ")

                        # If this is true that means that the user have already guessed all letters
                        if len(user_guessed_letters) == len(rand_word):
                            if lives == 1:
                                print("Congratulations you won with", lives, "life")
                            else:
                                print("Congratulations you won with", lives, "lives")
                                start = False
                                break

                # If the user entered something different than a single letter
                else:
                    print("Enter a single letter please")
                    # Printing the underscores with the guessed letters
                    for i in rand_word:
                        if i in user_guessed_letters:
                            print(i, end=" ")
                        else:
                            print("_", end=" ")

    def play_hangman():

        # Asking the user weather he wants to play or not
        while True:
            usr = input("So %s are you ready to begin (YES/NO): " % usr_name)

            if usr.upper() == "NO":
                print("Sorry to hear that...\nThanks for playing hangman\n")
                break

            elif usr.upper() == "YES":
                print("Great lets begin\n")
                hangman()
                # Asking the user to play one more time after the game has finished
                usr_choice = input("Y/YES if you want one more game, if not just press any key: ")
                if usr_choice.upper() == "Y" or usr_choice.upper() == "YES":
                    print("Okay great\n")
                    hangman()
                else:
                    print("Thanks for playing hangman\n")
                break

            else:
                print("%s is a wrong input try again\n" % usr)

    play_hangman()
