board = [" "] * 9


def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


winning_lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def has_won(player):
    for a, b, c in winning_lines:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


player = "X"

while True:
    show_board()
    try:
        spot = int(input("Player " + player + ", pick a spot 1-9: ")) - 1
    except ValueError:
        print("Please type a number!")
        continue

    if spot < 0 or spot > 8 or board[spot] != " ":
        print("You can't use that spot!")
        continue

    board[spot] = player

    if has_won(player):
        show_board()
        print("Player", player, "wins!")
        break

    if " " not in board:
        show_board()
        print("It's a tie!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"