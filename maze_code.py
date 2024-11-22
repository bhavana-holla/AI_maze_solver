
import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue

# A bigger maze
maze = [
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
]

def vis(m, start_point, goal_point, path=None):
    plt.figure(figsize=(8, 8))
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                plt.fill([j, j, j + 1, j + 1], [i, i + 1, i + 1, i], color='black')

    plt.plot(start_point[1] + 0.5, start_point[0] + 0.5, 'ro', markersize=12, label='Start')
    plt.plot(goal_point[1] + 0.5, goal_point[0] + 0.5, 'yo', markersize=12, label='Goal')

    if path:
        for (x, y) in path:
            plt.plot([y + 0.5, y + 0.5], [x + 0.5, x + 0.5], color='blue', lw=2)  
            plt.plot([y + 0.5, y + 0.5], [x + 0.5, x + 0.5], color='blue', lw=2)  
            if path.index((x, y)) < len(path) - 1:
                n_x, n_y = path[path.index((x, y)) + 1]
                plt.plot([y + 0.5, n_y + 0.5], [x + 0.5, n_x + 0.5], color='blue', lw=2)

    plt.xlim(0, len(m[0]))
    plt.ylim(len(m), 0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Maze Solution")
    plt.axis('off')
    plt.legend()
    plt.show()

def dfs(m, start_point, goal_point):
    stack, visited = [(start_point, [start_point])], set()
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal_point:
            return path
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(m) and 0 <= ny < len(m[0]) and
                m[nx][ny] == 0 and (nx, ny) not in visited):
                stack.append(((nx, ny), path + [(nx, ny)]))
    return None

def astar(m, start_point, goal_point):
    pq = PriorityQueue()
    pq.put((0, start_point, [start_point])) 
    visited = set()
    
    def h(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  
    
    while not pq.empty():
        c, (x, y), path = pq.get()
        if (x, y) == goal_point:
            return path
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(m) and 0 <= ny < len(m[0]) and
                m[nx][ny] == 0 and (nx, ny) not in visited):
                new_c = c + 1 + h((nx, ny), goal_point)
                pq.put((new_c, (nx, ny), path + [(nx, ny)]))
    return None

def get_input():
    start_point = (0, 0)  
    goal_point = (9, 9)   
    algo = input("Choose algo (dfs or astar): ").strip().lower()
    return start_point, goal_point, algo

def solve(m, start_point, goal_point, algo="dfs"):
    if algo == "dfs":
        path = dfs(m, start_point, goal_point)
    elif algo == "astar":
        path = astar(m, start_point, goal_point)
    else:
        print("Invalid algo choice.")
        return
    
    if path:
        print(f"Path found! Length: {len(path)}")
        vis(m, start_point, goal_point, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    start_point, goal_point, algo = get_input()
    solve(maze, start_point, goal_point, algo)
