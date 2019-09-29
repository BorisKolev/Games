"""
A small combination of games
Created: 03/01/2019
Author: Borislav Kolev
"""

# This is the main file from here you can choose which game to play
# The Games class is not really necessary, however I did it for fun
from Reach_Hundred import *
from Sink_The_Ship import *
from English_Dictionary import *
from Hangman import *


class Games:

    def __repr__(self):
        return "Games available::\n1.English dictionary, \n2.Hangman, \n3.Reach hundred, \n4.Sink the ship"

    @staticmethod
    def play_english_dictionary():
        dictionary()

    @staticmethod
    def play_hangman():
        hangman_game()

    @staticmethod
    def play_reach_hundred():
        play_100()

    @staticmethod
    def play_sink_the_ship():
        sink_the_ship()

    def play(self):
        while True:

            print(self)
            usr_choice = input("\nWrite the number corresponding to the game you want to play or 'Q' for quitting"
                               " the program:: ")

            if usr_choice == "1":
                self.play_english_dictionary()
                continue

            elif usr_choice == "2":
                self.play_hangman()
                continue

            elif usr_choice == "3":
                self.play_reach_hundred()
                continue

            elif usr_choice == "4":
                self.play_sink_the_ship()
                continue

            elif usr_choice.upper() == "Q" or usr_choice.upper() == "QUIT":
                print("Thanks for playing")
                break

            else:
                print("\n" + usr_choice + " is a wrong input try again\n")


player = Games()
player.play()
