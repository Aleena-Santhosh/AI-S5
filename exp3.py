def minimax(d, i, maxi, a, b):
    if d == h:
        return v[i]
    if maxi:
        best = -999
        for j in range(2):
            best = max(best, minimax(d+1, i*2+j, False, a, b))
            a = max(a, best)
            if a >= b:
                break
        return best
    else:
        best = 999
        for j in range(2):
            best = min(best, minimax(d+1, i*2+j, True, a, b))
            b = min(b, best)
            if a >= b:
                break
        return best
h = int(input("Height: "))
v = list(map(int, input(f"Enter {2**h} leaf values: ").split()))
print("Optimal value:", minimax(0, 0, True, -999, 999))