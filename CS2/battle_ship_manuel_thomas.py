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


def display_hidden_board(board):
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
        spot = input("Enter a spot: ").upper()

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


def get_player_move(board):
    while True:
        try:
            row = int(input("Please enter a guess, enter a row (1-5) "))
        except ValueError:
            print("Invalid selection, the row must be a number from 1-5 ")
            continue

        col = input("Please enter a guess, enter a column (A,B,C,D,E) ").upper()

        if row < 1 or row > 5:
            print("Please enter a row that is on the board, rows go from 1-5")
            continue

        if len(col) != 1 or col not in "ABCDE":
            print("Please enter a column that is on the board, columns go from A-E ")
            continue

        row = row - 1
        col = "ABCDE".index(col)

        if board[row][col] == "X" or board[row][col] == "O":
            print("You already guessed that spot, try again")
            continue

        return row, col


def place_ships(board):
    for i in range(3):
        print("Place ship " + str(i + 1))
        while True:
            row, col = player_guess()
            if board[row][col] == "S":
                print("You already have a ship there, pick another spot.")
                continue
            board[row][col] = "S"
            break
        display_board(board)


def computer_place_ships(board):
    placed = 0
    while placed < 3:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] != "S":
            board[row][col] = "S"
            placed += 1


def player_turn(board):
    row, col = get_player_move(board)
    spot = "ABCDE"[col] + str(row + 1)

    if board[row][col] == "S":
        board[row][col] = "X"
        print("You guessed " + spot + " and it Hit!")
    else:
        board[row][col] = "O"
        print("You guessed " + spot + " and it Missed.")


def computer_guess(board):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)

        if board[row][col] == "X" or board[row][col] == "O":
            continue

        spot = "ABCDE"[col] + str(row + 1)

        if board[row][col] == "S":
            board[row][col] = "X"
            print("The Computer guessed " + spot + " and it Hit!")
        else:
            board[row][col] = "O"
            print("The Computer guessed " + spot + " and it Missed.")

        return


def ships_left(board):
    for row in board:
        if "S" in row:
            return True
    return False


def play_game():
    player_board = [["~"] * 5 for _ in range(5)]
    computer_board = [["~"] * 5 for _ in range(5)]

    display_board(player_board)
    place_ships(player_board)
    computer_place_ships(computer_board)

    while True:
        print("Computer's board:")
        display_hidden_board(computer_board)
        player_turn(computer_board)

        if not ships_left(computer_board):
            display_board(computer_board)
            print("You sank all the computer's ships. You win!")
            break

        computer_guess(player_board)
        print("Your board:")
        display_board(player_board)

        if not ships_left(player_board):
            print("The computer sank all your ships. You lose!")
            break


play_game()
