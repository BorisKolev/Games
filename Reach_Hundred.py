from random import randint

"""
Reach a hundred first
Created: 17/12/2018
Author: Borislav Kolev
"""

"""
In this game you are playing against the computer each turn you or the computer has to pick a number between 1 to 10
whoever reaches 100 first will win, In order to beat the computer you have to understand the pattern in which the
computer is picking the numbers and pick it yourself, otherwise the computer will always win.
"""


def play_100():

    print("#### Welcome to reach a hundred ####\n")
    the_number = 0

    # Game ends when the computer or the player reaches 100
    while the_number < 100:

        # The full pattern of numbers you have to keep reaching
        # full_pattern = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]

        # Half of the pattern of numbers you have to keep reaching
        # It is better to use that one since it will be harder for the player to figure out the pattern
        half_pattern = [45, 56, 67, 78, 89, 100]

        while True:
            try:
                usr = int(input("Enter a digit from 1 to 10 :: "))

            # If the user does not enter a number
            except ValueError:
                print("You did not enter a number")

            else:
                # adding the user's number to the_number only if it is between 1 and 10
                if usr in range(1, 11):
                    the_number += usr
                    print("Sum is:: " + str(the_number))

                    # Checking if the user reached 100
                    if the_number >= 100:
                        print("Congratulations you solved it\n")
                        usr = input("If you want to play again press any key, if not write 'NO':: ")
                        if usr.upper() == "NO":
                            print("Thanks for playing reach a hundred\n")

                        else:
                            print()
                            play_100()

                    # Break of the inner while loop so that now computer can choose a number
                    break

        inx = 0
        for i in half_pattern:

            # Reach next patter value in line
            if i > the_number:

                # The computer next choice will be a number with which it will reach the next pattern value
                comp_choice = half_pattern[inx] - the_number

                # In case the user has entered correct number e.g.
                # ( The computer needs 11 to reach the next pattern value )
                # It will pick a random value
                if comp_choice > 10:
                    comp_choice = randint(1, 10)

                print("Computer choice is:: " + str(comp_choice))
                the_number += comp_choice
                print("Sum is:: " + str(the_number))

                if the_number >= 100:
                    print("The computer won, try again")
                    usr = input("If you want to play again press any key, if not write 'NO':: ")
                    if usr.upper() == "NO":
                        print("Thanks for playing reach a hundred\n")
                        break
                    else:
                        print()
                        play_100()
                break

            else:
                inx += 1
