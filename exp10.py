nodes_pruned = 0
def alpha_beta(depth, index, alpha, beta, maximizing_player, leaf_values):
    global nodes_pruned
    if depth == 4:
        if index < len(leaf_values):
            return leaf_values[index]
        else:
            return None
    if maximizing_player:
        best = float('-inf')
        for i in [1, 0]:
            child_index = index * 2 + i
            if depth + 1 == 4 and child_index >= len(leaf_values):
                continue
            value = alpha_beta(depth + 1,child_index,alpha,beta,False,leaf_values)
            if value is None:
                continue
            best = max(best, value)
            alpha = max(alpha, best)
            if alpha >= beta:
                nodes_pruned += 1
                break
        return best
    else:
        best = float('inf')
        for i in [1, 0]:
            child_index = index * 2 + i
            if depth + 1 == 4 and child_index >= len(leaf_values):
                continue
            value = alpha_beta(depth + 1,child_index,alpha,beta,True,leaf_values)
            if value is None:
                continue
            best = min(best, value)
            beta = min(beta, best)
            if alpha >= beta:
                nodes_pruned += 1
                break
        return best
leaf_values = list(map(int, input(
    "Enter leaf node values separated by spaces: "
).split()))
print("\nLeaf node values:", leaf_values)
print("Number of leaf nodes entered:", len(leaf_values))
result = alpha_beta(0,0,float('-inf'),float('inf'),False,leaf_values)
print("Root value:", result)
print("Final MINIMAX value:", result)
print("Number of pruned branches:", nodes_pruned)