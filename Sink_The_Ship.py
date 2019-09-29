"""
Hangman
Created: 14/11/2018
Author: Borislav Kolev
"""

from random import randint
from time import sleep


def sink_the_ship():
    # This function will print the board with only the O's in it

    def print_board(board):
        for l in board:
            print(" ".join(l))

    # Those two functions will place the ship in a random column and a row

    def random_row(board):
        rand_row = randint(0, len(board)-1)
        return rand_row

    def random_col(board):
        rand_col = randint(0, len(board)-1)
        return rand_col

    print("\n\t### WELCOME TO BATTLESHIP ###\n")
    usr_choice = input("  Do you want to play alone (Y/N)? :: ")
    usr_choice = usr_choice.upper()
    wrong_input = True

    # In case user enters a wrong input
    while wrong_input:

        # If the user wants to play ALONE
        if usr_choice == "Y" or usr_choice == "YES":

            play = True
            while play:

                # Creating two, five by five grids
                the_board = []
                brand_new_board = []
                for i in range(5):
                    the_board.append(["O"] * 5)
                    brand_new_board.append(["0"] * 5)

                lives = 3

                print("\nThe ship is hidden in the sea you have to try and sink it")
                sleep(2)
                print("You have ", lives, " lives")
                sleep(1)

                # This will be the random allocation of the ship
                ship_row = random_row(the_board)
                ship_col = random_col(the_board)

                # You can use the code below to see where the ship is located
                # print(ship_row)
                # print(ship_col)

                print()
                print_board(the_board)
                print()

                # In this while loop the player plays the game
                while lives > 0:

                    # Trying to hit the ship
                    try:
                        sleep(1)
                        guess_row = int(input("Guess a row from 1 to 5:: "))
                        guess_row -= 1
                        guess_col = int(input("Guess a col from 1 to 5:: "))
                        guess_col -= 1

                    except ValueError:
                        print("\nPlease enter A NUMBER from 1 to 5\n ")

                    else:
                        # If the user enters outside of the grid
                        if guess_row > len(the_board) - 1 or guess_row < 0 or guess_col > len(the_board) - 1 or \
                                guess_col < 0:
                            print("\nThat is not even in the sea\n")
                            continue

                        # If the user tries the same locations twice
                        elif the_board[guess_row][guess_col] == "X":
                            sleep(1)
                            print("\nYou already tried that one\n")
                            sleep(1)
                            print_board(the_board)
                            print()
                            continue

                        # If the user guess the location
                        elif ship_row == guess_row and ship_col == guess_col:
                            sleep(1)
                            print("\nYou sank the battleship\n")
                            # Making all the grid full of X-es and only the ship O
                            for i in range(len(the_board)):
                                for j in range(len(the_board)):
                                    if i == guess_row and j == guess_col:
                                        the_board[i][j] = "O"
                                    else:
                                        the_board[i][j] = "X"
                            print_board(the_board)

                            sleep(1)
                            # Asking if the user wants to play again
                            usr_choice = input("\nYou successfully sank the battleship and won,"
                                               "\nif you want to play again press any key"
                                               "\nif you want to leave write 'quit':: ")
                            usr_choice = usr_choice.upper()
                            if usr_choice == "QUIT":
                                print("Thanks for playing sink the ship\n")
                                wrong_input = False
                                play = False
                                break
                            else:
                                break

                        # User misses
                        else:
                            sleep(1)
                            print("\nYou missed the battleship\n")
                            # Turning the 'O' into 'X' where the missed allocation is and taking one live
                            the_board[guess_row][guess_col] = "X"
                            sleep(1)
                            print_board(the_board)
                            lives -= 1
                            print()
                            print(lives, " lives left\n")

                            if lives == 0:
                                sleep(2)
                                print("Game over")
                                sleep(1)
                                # Using the brand_new_board to show where the ship was after the user has been defeated
                                print("The ship was here:: \n")
                                print("row ::", ship_row + 1)
                                print("column ::", ship_col + 1)
                                brand_new_board[ship_row][ship_col] = "X"
                                print_board(brand_new_board)

                                # Asking the player whether he wants to play again
                                usr_choice = input("\nYou were defeated"
                                                   "\nif you want to play again press any key"
                                                   "\nif you want to leave write 'quit':: ")
                                usr_choice = usr_choice.upper()

                                if usr_choice == "QUIT":
                                    print("Thanks for playing sink the ship\n")
                                    wrong_input = False
                                    play = False
                                    break
                                else:
                                    break

        # If the user wants to play with a friend
        elif usr_choice == "N" or usr_choice == "NO":

            player1 = input("\nPlayer 1 enter a name:: ")
            player2 = input("\nPlayer 2 Enter a name:: ")

            play = True
            while play:

                # It will increment and keep track of which player the turn is
                x = 0
                the_board = []

                for i in range(5):
                    the_board.append(["O"] * 5)

                sleep(1)
                print("\nOkay, ", player1, " and ", player2)
                print("The ship is hidden in the sea you have to try and sink it")
                sleep(1)
                print("Whoever sink it first wins")

                # Getting the random values for the row and the column
                ship_row = random_row(the_board)
                ship_col = random_col(the_board)

                # You can use this code to see the location of the ship
                # print(ship_row)
                # print(ship_col)

                sleep(1)
                print()
                print_board(the_board)
                print()

                while True:

                    # If the number is even it will be the first player turn
                    if x % 2 == 0:
                        try:
                            sleep(1)
                            guess_row = int(input(player1 + " Guess a row from 1 to 5:: "))
                            guess_row -= 1
                            guess_col = int(input(player1 + " Guess a col from 1 to 5:: "))
                            guess_col -= 1
                            x += 1

                        except ValueError:
                            print("Enter a number")
                            continue

                    # If the number is odd it will be the second player turn
                    else:
                        try:
                            sleep(1)
                            guess_row = int(input(player2 + " Guess a row from 1 to 5:: "))
                            guess_row -= 1
                            guess_col = int(input(player2 + " Guess a col from 1 to 5:: "))
                            guess_col -= 1
                            x += 1

                        except ValueError:
                            print("Enter a number")
                            continue

                    # If the user enters outside of the grid
                    if guess_row > len(the_board) - 1 or guess_row < 0 or guess_col > len(the_board) - 1 \
                            or guess_col < 0:
                        print("\nThat is not even in the sea\n")
                        continue

                    # If the user tries the same locations twice
                    elif the_board[guess_row][guess_col] == "X":
                        print("\nYou already tried that one\n")
                        sleep(1)
                        print_board(the_board)
                        print()
                        continue

                    # If the user guess the location
                    elif ship_row == guess_row and ship_col == guess_col:
                        sleep(1)
                        print("\nYou sank the battleship \n")
                        # Making all the grid full of X-es and only the ship O
                        for i in range(len(the_board)):
                            for j in range(len(the_board)):
                                if i == guess_row and j == guess_col:
                                    the_board[i][j] = "O"
                                else:
                                    the_board[i][j] = "X"
                        sleep(1)
                        print_board(the_board)

                        if x % 2 == 0:
                            print()
                            usr_choice = input(player1 + " You were defeated"
                                               "\nif you want to play again press any key"
                                               "\nif you want to leave write 'quit':: ")
                        else:
                            print()
                            usr_choice = input(player2 + " You were defeated"
                                               "\nif you want to play again press any key"
                                               "\nif you want to leave write 'quit':: ")
                        usr_choice = usr_choice.upper()

                        if usr_choice == "QUIT":
                            print("Thanks for playing sink the ship\n")
                            wrong_input = False
                            play = False
                            break
                        else:
                            print()
                            break

                    else:
                        sleep(1)
                        print("\nYou missed the battleship\n")
                        the_board[guess_row][guess_col] = "X"
                        sleep(1)
                        print_board(the_board)
                        print()

        else:
            print()
            print(usr_choice, " is a wrong input\n")
            usr_choice = input("Do you want to play alone (Y/N)? :: ")
            usr_choice = usr_choice.upper()
