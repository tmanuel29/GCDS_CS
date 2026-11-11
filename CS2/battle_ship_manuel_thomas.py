import random

def display_board(board):
    size = len(board)

    header = "   "
    for col in range(size):
        header += chr(65 + col) + " "   
    print(header)

  
    for i in range(size):
        row_label = str(i + 1).rjust(2)  
        print(row_label + " " + " ".join(board[i]))


board = [["~"] * 5 for _ in range(5)]


display_board(board)



def display_hidden_board():
    hidden = []
    for row in board:
        new_row = []
        for spot in row:
            if spot == "S":
                new_row.append("~")
            else:
                new_row.append(spot)
        hidden.append(new_row)
    display_board(hidden)






def player_guess():
    while True:
        spot = input("Enter a spot: ").lower()

        if len(spot) != 2:
            print("Error: enter one letter and one number, like B3.")
            continue

        col = ord(spot[0]) - 65
        if col < 0 or col > 4:
            print("Error: letter must be A to E.")
            continue

        if not spot[1].isdigit():
            print("Error: second character must be a number.")
            continue

        row = int(spot[1]) - 1
        if row < 0 or row > 4:
            print("Error: number must be 1 to 5.")
            continue

        return row, col




def computer_guess(board):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)

        if board[row][col] == "X" or board[row][col] == "O":
            continue

        spot = "ABCDE"[col] + str(row + 1)

        if board[row][col] == "S":
            board[row][col] = "X"
            print("The Computer guessed and " + spot + " it Hit!")
        else:
            board[row][col] = "O"
            print("The Computer guessed and " + spot + " it Missed.")

        return



def get_player_move(board):
    while True:
        try:
            row = int(input("Please enter a guess, enter a row (1-5)  "))
            col = int(input("Please enter a guess, enter a column (A,B,C,D,E) "))
        except ValueError:
            print("Invalid selection, please enter the correct numbers and letter for rows and columns")

            continue

        if row < 1 or row > 5 or col < 1 or col > 5:
            print("Plese enter a number that is on the board, rows go from 1-5 and columns from A-E ")

            
