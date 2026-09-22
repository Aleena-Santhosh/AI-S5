def valid(g, r, c, n):
    for i in range(9):
        if g[r][i] == n or g[i][c] == n:
            return False
    br = r // 3 * 3
    bc = c // 3 * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if g[i][j] == n:
                return False
    return True
def solve(g):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                for n in range(1, 10):
                    if valid(g, r, c, n):
                        g[r][c] = n
                        if solve(g):
                            return True
                        g[r][c] = 0
                return False
    return True
g = []
print("Enter Sudoku (use 0 for empty cells):")
for i in range(9):
    g.append(list(map(int, input().split())))
if solve(g):
    print("\nSolved Sudoku:")
    for row in g:
        print(*row)
else:
    print("No solution")