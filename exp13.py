import random
current = int(input("Enter current value: "))
neighbors = list(map(int, input("Enter neighbor values: ").split()))
# Simple Hill Climbing
simple = current
for n in neighbors:
    if n > simple:
        simple = n
        break
# Steepest-Ascent Hill Climbing
steepest = current
best = max(neighbors)
if best > steepest:
    steepest = best
# Stochastic Hill Climbing
better = [n for n in neighbors if n > current]
stochastic = random.choice(better) if better else current
print("\nSimple Hill Climbing:", simple)
print("Steepest-Ascent Hill Climbing:", steepest)
print("Stochastic Hill Climbing:", stochastic)