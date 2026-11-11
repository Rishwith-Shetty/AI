
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for positions in win_positions:
        if all(board[i] == player for i in positions):
            return True

    return False


def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Choose a position from 1 to 9.")

    while True:
        print_board(board)
        print(f"Player {player}'s turn")

        try:
            position = int(input("Enter position (1-9): "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if position < 1 or position > 9:
            print("Invalid position! Try again.")
            continue

        if board[position - 1] in ["X", "O"]:
            print("Position already taken! Try again.")
            continue

        board[position - 1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(cell in ["X", "O"] for cell in board):
            print_board(board)
            print("It's a Draw!")
            break

        player = "O" if player == "X" else "X"


tic_tac_toe()

