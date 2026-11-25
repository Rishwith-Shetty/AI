import math


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    name = node["name"]

    # Base case: leaf node or maximum depth reached
    if depth == 0 or not node["children"]:
        print(f"Leaf {name} -> value: {node['value']}")
        return node["value"]

    role = "MAX" if maximizing_player else "MIN"
    print(f"Visiting {name} ({role}) | alpha: {alpha}, beta: {beta}")

    if maximizing_player:
        max_eval = -math.inf
        for child in node["children"]:
            eval_score = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            print(f"  {name} updated -> max_eval: {max_eval}, alpha: {alpha}")
            if beta <= alpha:
                print(
                    f"  [PRUNED] Beta cut-off at {name} (beta {beta} <= alpha {alpha})"
                )
                break
        return max_eval

    else:
        min_eval = math.inf
        for child in node["children"]:
            eval_score = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            print(f"  {name} updated -> min_eval: {min_eval}, beta: {beta}")
            if beta <= alpha:
                print(
                    f"  [PRUNED] Alpha cut-off at {name} (beta {beta} <= alpha {alpha})"
                )
                break
        return min_eval


# Example game tree with named nodes
game_tree = {
    "name": "Root",
    "value": None,
    "children": [
        {
            "name": "B",
            "value": None,
            "children": [
                {"name": "D", "value": 3, "children": []},
                {"name": "E", "value": 5, "children": []},
                {"name": "F", "value": 6, "children": []},
            ],
        },
        {
            "name": "C",
            "value": None,
            "children": [
                {"name": "G", "value": 1, "children": []},
                {"name": "H", "value": 2, "children": []},  # Pruned
                {"name": "I", "value": 9, "children": []},  # Pruned
            ],
        },
        {
            "name": "J",
            "value": None,
            "children": [
                {"name": "K", "value": 12, "children": []},
                {"name": "L", "value": 8, "children": []},
                {"name": "M", "value": 4, "children": []},
            ],
        },
    ],
}

best_score = alpha_beta(
    game_tree, depth=3, alpha=-math.inf, beta=math.inf, maximizing_player=True
)
print(f"\nOptimal value at Root: {best_score}")


