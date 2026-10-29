'''

Name:        Thomas Manuel
Date:        10/19/26
Description: A two-player Tic-Tac-Toe game that runs in
             the terminal.
Extensions:


Plan work, work plan

step 1: create a 2 dimensional grid that has 3 columns and rows
step 2: Two human players
step 3: have to determine who goes first - random choice
step 4: person going first gets to choose whether they go x or o
step 5: ask player one where they would like to go, top left/ row 1, spot 1 etc.
step 6: check to see if a player has won - diagonal - vertical - horizontal
step 7: create a function called check win to see who won the game
step 8: also make it for a tie
step 9: at the end of game clear board - ask to play again - quit
'''

import random


def display_board(board):
    """
    Description: Print the current board to the terminal with row and
    column numbers so players can see where to move.

    Args:
    - board: a 3x3 list of lists holding "X", "O", or " " in each spot
    """

    print("   1   2   3")
    
    for i in range(3):
        row = board[i]
        print(str(i + 1) + "  " + row[0] + " | " + row[1] + " | " + row[2])
        if i < 2:
            print("  ---+---+---")


def check_winner(board, mark):
    """
    Description: Check whether the given mark has three in a row
    horizontally, vertically, or diagonally.

    Args:
    - board: a 3x3 list of lists holding "X", "O", or " " in each spot
    - mark: the player's mark to check for, either "X" or "O"

    Returns:
    - bool: True if that mark has won, False otherwise
    """

    for i in range(3):
   
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:

            return True
     
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:

            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:

        return True
    
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:

        return True

    return False


def is_draw(board):
    """
    Description: Check whether the board is full with no empty spots left,
    meaning the game is a tie (if no one has won).

    Args:
    - board: a 3x3 list of lists holding "X", "O", or " " in each spot

    Returns:
    - bool: True if every spot is filled, False if any spot is empty
    """
   
    for row in board:
        if " " in row:
            return False
    return True


def choose_first():
    """
    Description: Ask for both players' names, then randomly pick who
    goes first and announce it.

    Returns:
    - tuple: (first player's name, second player's name)
    """

    players = [input("Player 1 name: "), input("Player 2 name: ")]

    random.shuffle(players) 

    print(players[0] + " goes first!")

    return players[0], players[1]


def get_player_move(board, mark):
    """
    Description: Ask the player for a row and column and keep asking
    until they enter a valid, empty spot. Handles non-number input,
    out-of-range numbers, and spots that are already taken.

    Args:
    - board: a 3x3 list of lists holding "X", "O", or " " in each spot
    - mark: the current player's mark, either "X" or "O"

    Returns:
    - tuple: (row index, column index) of the chosen spot, each 0-2
    """
  
    while True:
        try:
            row = int(input("Player " + mark + ", enter a row (1-3): "))

            col = int(input("Player " + mark + ", enter a column (1-3): "))
        except ValueError:

            print("Invalid input. Please enter numbers only.")

            continue


        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Out of range. Rows and columns go from 1 to 3.")

        elif board[row - 1][col - 1] != " ":

            print("That spot is already taken. Pick another one.")
        
        else:
            return row - 1, col - 1 


def play_game():
    """
    Description: Run the main game loop. Sets up a new board, picks who
    goes first, lets them choose X or O, alternates turns until someone
    wins or it's a tie, then asks if the players want to play again.
    """

    while True:

        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        first, second = choose_first()

       
        first_mark = input(first + ", choose X or O: ").upper()

        while first_mark != "X" and first_mark != "O":

            first_mark = input("Invalid. Please type X or O: ").upper()

        if first_mark == "X":

            second_mark = "O"

        else:
            second_mark = "X"

        turn = 0

        while True:
            
            if turn % 2 == 0:
                player, mark = first, first_mark

            else:
                player, mark = second, second_mark

            display_board(board)
            print(player + "'s turn (" + mark + ")")
            row, col = get_player_move(board, mark)
            board[row][col] = mark


            if check_winner(board, mark):
                result = player + " wins!"
                break
            if is_draw(board):
                result = "It's a tie!"
                break


            turn += 1


        display_board(board)
        print(result)


        while True:
            again = input("Play again? yes or no: ").lower()
            if again.startswith("y"):
                break
            elif again.startswith("n"):
                print("Thanks for playing!")
                return
            else:
                print("Invalid response, please choose yes or no ")


if __name__ == "__main__":
    play_game()
