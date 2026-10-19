'''
***
* Name:        Thomas Manuel
* Date:        10/19/26
* Description: A two-player Tic-Tac-Toe game that runs in
*              the terminal.
* Extensions:
***

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
    print("   1   2   3")
    for i in range(len(board)):
        print(str(i + 1) + "  " + " │ ".join(board[i]) + " ")
        if i < len(board) - 1:
            print("  ───┼───┼───")


def check_winner(board, mark):
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True

    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False


def is_draw(board):
    for row in board: 
        for cell in row:
            if cell == " ":
                return False
    return True


def choose_first():
    player1 = input("Player number 1 name: ")
    player2 = input("Player number 2 name: ")

    first = random.choice([player1, player2])

    if first == player1:
        second = player2
    else:
        second = player1
    print(first + " goes first!")
    return first, second


def get_player_move(board, player):
  
    while True:
        row = input("Player " + player + ", enter a row (1-3): ")
        col = input("Player " + player + ", enter a column (1-3): ")

        
        try:
            row = int(row)
            col = int(col)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

       
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Out of range. Rows and columns go from 1 to 3.")
            continue

        
        if board[row - 1][col - 1] != " ":
            print("That spot is already taken. Pick another one.")
            continue

        return row - 1, col - 1


def play_game():
  
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
                current_player = first
                current_mark = first_mark
            else:
                current_player = second
                current_mark = second_mark

            display_board(board)
            print(current_player + "'s turn (" + current_mark + ")")

            row, col = get_player_move(board, current_mark)
            board[row][col] = current_mark

       
            if check_winner(board, current_mark):
                display_board(board)
                print(current_player + " wins!")
                break

            if is_draw(board):
                display_board(board)
                print("It's a tie!")
                break

            turn += 1

        again = input("Play again? yes or no: ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
