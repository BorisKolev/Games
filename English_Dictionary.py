"""
English Dictionary
Created: 13/10/2018
Author: Borislav Kolev
"""

# Importing the json library
import json
from difflib import get_close_matches

# collection.json file stores the information in a dictionary
# The keys are the words and the values are the meaning of the words
# The values of the dictionary are stored in lists

collection = json.load(open("data/collection.json"))


def find_word(the_word):
    # The word that the user is looking for
    the_word = the_word.lower()

    # If it directly finds the word
    if the_word in collection:
        # return the meaning in a LIST
        return collection[the_word]

    # If the word is spelled wrong get_close_matches will try to make a list with all close words
    elif len(get_close_matches(the_word, collection.keys())) > 0:

        # Outputting the list of possible matches to the user
        question = input("Is the word you are looking for here\n%s ? \n(Y/N):: "
                         % get_close_matches(the_word, collection.keys()))

        # If user recognize the word
        if question.upper() == "Y" or question.upper() == "YES":
            the_word = input("Write the word: ")

            # Check if the word is in the list of the matched words
            if the_word in get_close_matches(the_word, collection.keys()):
                return collection[the_word]

            else:
                print("You misspelled the word")
                return None

        elif question.upper() == "N" or question.upper() == "NO":
            print("Word was not found")
            return None

        else:
            print("Wrong input")
            return None

    else:
        print("Word was not found")
        return None


# This function keeps calling the find_word function
def dictionary():
    start = True

    print("\n#### Welcome to the English dictionary####")
    while start:

        print("\nYou can enter Q to quit")
        word = input("Enter word you are looking for:: ")
        # The while loop will stop if the user enters Q
        if word.upper() == "Q" or word.upper() == "QUIT":
            start = False
            print("Thanks for using the english dictionary\n")

        else:
            # The output is a returned list with one or more items (each item is meaning of the word)
            list_of_meanings = find_word(word)

            # It will repeat the while loop
            if list_of_meanings is None:
                print("Try again")

            # The function has found the word
            elif list_of_meanings is not None:
                # Printing the meanings of the word
                for meaning in list_of_meanings:
                    print(meaning)
