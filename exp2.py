import heapq
graph = {'A': [('B', 1), ('C', 3)],'B': [('D', 3), ('E', 6)],'C': [('F', 5)],
    'D': [('G', 2)],'E': [('G', 1)],'F': [('G', 2)],'G': []}
# Heuristic values 
heuristic = {'A': 6,'B': 5,'C': 4,'D': 2,'E': 1,'F': 2,'G': 0}
def astar(start, goal):
    # Priority Queue
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()
    while open_list:
        # Get node with lowest f(n)
        f_cost, g_cost, current, path = heapq.heappop(open_list)
        # If goal is reached
        if current == goal:
            return path, g_cost
        # Skip already visited nodes
        if current in visited:
            continue
        visited.add(current)
        # Explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g_cost = g_cost + cost
                new_f_cost = new_g_cost + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f_cost, new_g_cost, neighbor, path + [neighbor])
                )
    return None, None
# Main Program
start = 'A'
goal = 'G'
result = astar(start, goal)
if result[0]:
    path, cost = result
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")