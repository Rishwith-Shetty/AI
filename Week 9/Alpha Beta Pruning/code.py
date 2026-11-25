import math


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    # Base case: leaf node or maximum search depth reached
    if depth == 0 or not node["children"]:
        return node["value"]

    if maximizing_player:
        max_eval = -math.inf
        for child in node["children"]:
            eval_score = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval

    else:
        min_eval = math.inf
        for child in node["children"]:
            eval_score = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval


# Example game tree (depth 3)
game_tree = {
    "value": None,
    "children": [
        {
            "value": None,
            "children": [
                {"value": 3, "children": []},
                {"value": 5, "children": []},
                {"value": 6, "children": []},
            ],
        },
        {
            "value": None,
            "children": [
                {"value": 1, "children": []},
                {"value": 2, "children": []},
                {"value": 9, "children": []},
            ],
        },
        {
            "value": None,
            "children": [
                {"value": 12, "children": []},
                {"value": 8, "children": []},
                {"value": 4, "children": []},
            ],
        },
    ],
}

best_score = alpha_beta(
    game_tree, depth=3, alpha=-math.inf, beta=math.inf, maximizing_player=True
)
print("Optimal value:", best_score)  # Output: 4
