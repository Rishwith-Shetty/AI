# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# Depth Limited Search
def dls(state, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = dls(neighbor, depth - 1, path + [neighbor])

            if result:
                return result

    return None


# Iterative Deepening Search
def ids(start, max_depth):
    for depth in range(max_depth + 1):
        print("Searching at depth:", depth)

        result = dls(start, depth, [start])

        if result:
            print("\nSolution Found!\n")

            for state in result:
                print(state[:3])
                print(state[3:6])
                print(state[6:])
                print()

            print("Total moves:", len(result) - 1)
            return

    print("Solution not found within maximum depth!")


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

ids(start, 10)
