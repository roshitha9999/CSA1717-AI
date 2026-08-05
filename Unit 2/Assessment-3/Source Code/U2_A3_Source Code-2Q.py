import math


def minimax(tree, depth, is_maximizing, alpha, beta, path_label=""):

    # Leaf level: tree[node_index] holds the leaf values for a MIN node.
    if depth == 1:
        leaves = tree
        best = math.inf
        for i, value in enumerate(leaves):
            print(f"  Evaluating leaf {path_label}[{i}] = {value}")
            best = min(best, value)
            beta = min(beta, best)
            print(f"    Alpha = {alpha}, Beta = {beta}")
            if beta <= alpha:
                pruned = leaves[i + 1:]
                if pruned:
                    print(f"    Pruned remaining leaves of {path_label} : {pruned}")
                break
        print(f"  Selected value for {path_label} = {best}")
        return best

    best = -math.inf
    child_values = []

    for idx, subtree in enumerate(tree):
        label = f"MIN-{idx + 1}"
        print(f"\n---- Evaluating {label} ----")
        value = minimax(subtree, depth - 1, False, alpha, beta, label)
        child_values.append(value)
        best = max(best, value)
        alpha = max(alpha, best)
        print(f"After {label}: Alpha updated to {alpha}")

    return best, child_values


while True:

    print("\nEnter the leaf node values")

    l1 = int(input("Leaf 1 : "))
    l2 = int(input("Leaf 2 : "))
    l3 = int(input("Leaf 3 : "))
    r1 = int(input("Leaf 4 : "))
    r2 = int(input("Leaf 5 : "))
    r3 = int(input("Leaf 6 : "))

    tree = [[l1, l2, l3], [r1, r2, r3]]

    print("\n====================================")
    final_value, values = minimax(tree, 2, True, -math.inf, math.inf)

    print("\n====================================")
    print("Values returned to MAX :", values)
    print("Final Minimax Value :", final_value)

    if final_value == values[0]:
        print("Best Move : Left Subtree")
    else:
        print("Best Move : Right Subtree")

    ch = input("\nRun Again?(y/n): ")

    if ch.lower() != 'y':
        break
