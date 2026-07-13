from collections import deque
goal_state = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
def print_state(state):
    for row in state:
        print(row)
    print()
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]     
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors
def is_goal(state):
    return state == goal_state
def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])     
    while queue:
        state, path = queue.popleft()
        state_tuple = tuple(tuple(row) for row in state)        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)        
        if is_goal(state):
            return path + [state]        
        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))    
    return None
print("Enter the initial puzzle state row by row (use 0 for blank):")
start_state = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    start_state.append(row)
print("\nInitial State")
print_state(start_state)
solution = bfs(start_state)
if solution:
    print("Solution Found")
    print("Number of moves =", len(solution)-1)
    for i, state in enumerate(solution):
        print("Step", i)
        print_state(state)
else:
    print("No solution exists.")