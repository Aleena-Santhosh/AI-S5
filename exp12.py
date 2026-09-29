n = int(input("Enter number of cities: "))
cities = input("Enter city names: ").split()
print("Enter distance matrix:")
dist = [list(map(int, input().split())) for _ in range(n)]
tour = list(range(n))
def cost(t):
    return sum(dist[t[i]][t[(i+1) % n]] for i in range(n))
while True:
    best = tour[:]
    for i in range(1, n):
        for j in range(i + 1, n):
            new = tour[:]
            new[i], new[j] = new[j], new[i]
            if cost(new) < cost(best):
                best = new
    if cost(best) >= cost(tour):
        break
    tour = best
print("Final Tour:", " -> ".join(cities[i] for i in tour))
print("Total Distance:", cost(tour))