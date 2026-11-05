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
