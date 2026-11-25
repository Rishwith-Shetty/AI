import random

N = 4

# Calculate number of attacking queen pairs
def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Hill Climbing Algorithm
def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current = heuristic(board)

        if current == 0:
            return board

        best_board = board
        best_value = current

        for col in range(N):
            for row in range(N):
                if row != board[col]:
                    new_board = board.copy()
                    new_board[col] = row

                    value = heuristic(new_board)

                    if value < best_value:
                        best_value = value
                        best_board = new_board

        if best_value >= current:
            board = [random.randint(0, N - 1) for _ in range(N)]
        else:
            board = best_board


# Display chessboard
solution = hill_climbing()

print("Solution Found:")
for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()

print("Number of conflicts:", heuristic(solution))
