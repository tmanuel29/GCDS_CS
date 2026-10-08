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
def display_board(board):
    for row in board:
        print(" | ".join(row))

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

display_board(game_board)
input()