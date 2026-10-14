#Plan work, work plan
'''


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
    for i in range(len(board)):
        print(" " + " │ ".join(board[i]) + " ")
        if i < len(board) - 1:
            print("───┼───┼───")



display_board(game_board)
input()

def checkwinner(board, complete):


    if board[0][0] == complete and board[0][1] == complete and board[0][2]== complete: 
        return True
    if board[1][0] == complete and board[1][1] == complete and board[1][2] == complete:
        return True
    if board[2][0] == complete and board[2][1] == complete and board[2][2] == complete:
        return True


    if board[0][0] == complete and board[0][1] == complete and board[0][2]== complete: 
            return True
    if board[0][1] == complete and board[1][1] == complete and board[2][1] == complete:
            return True
    if board[0][2] == complete and board[1][2] == complete and board[2][2] == complete:
            return True

    if board[0][0] == complete and board[1][1] == complete and board[2][2] == complete:
         return True
    if board[0][2] == complete and board[1][1] == complete and board[2][0] == complete:
         return True


def tie_checker(board):
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
    print(first + "goes first! ")
    return first, second


if __name__ == "__main__":
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    first, second = choose_first()
    display_board(game_board)
