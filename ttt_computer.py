import random

board = [" "] * 9

winning_lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def show_board():
    cells = [board[i] if board[i] != " " else str(i + 1) for i in range(9)]
    print()
    print(cells[0], "|", cells[1], "|", cells[2])
    print("--+---+--")
    print(cells[3], "|", cells[4], "|", cells[5])
    print("--+---+--")
    print(cells[6], "|", cells[7], "|", cells[8])
    print()


def has_won(player):
    for a, b, c in winning_lines:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


def free_spots():
    return [i for i in range(9) if board[i] == " "]


def find_winning_spot(player):
    for spot in free_spots():
        board[spot] = player
        won = has_won(player)
        board[spot] = " "
        if won:
            return spot
    return None


def computer_move():
    spot = find_winning_spot("O")
    if spot is None:
        spot = find_winning_spot("X")
    if spot is None and board[4] == " ":
        spot = 4
    if spot is None:
        corners = [i for i in (0, 2, 6, 8) if board[i] == " "]
        if corners:
            spot = random.choice(corners)
    if spot is None:
        spot = random.choice(free_spots())
    board[spot] = "O"
    print("Computer picks", spot + 1)


def player_move():
    while True:
        try:
            spot = int(input("Your turn (X), pick 1-9: ")) - 1
        except ValueError:
            print("Please type a number!")
            continue
        if spot < 0 or spot > 8 or board[spot] != " ":
            print("You can't use that spot!")
            continue
        board[spot] = "X"
        return


def play():
    board[:] = [" "] * 9

    while True:
        show_board()
        player_move()
        if has_won("X"):
            show_board()
            print("You win! Amazing!")
            return
        if not free_spots():
            show_board()
            print("It's a tie!")
            return

        computer_move()
        if has_won("O"):
            show_board()
            print("Computer wins! Try again!")
            return
        if not free_spots():
            show_board()
            print("It's a tie!")
            return


while True:
    play()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Bye!")
        break