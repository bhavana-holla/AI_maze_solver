# AI_maze_solver
A Python program that implements a pathfinding algorithm (DFS or A*) to solve mazes represented as 2D grids. The project includes visualization using Matplotlib, showcasing the maze layout, obstacles, and the final solution path.

## Prerequisites:
* Python 3.x
* Matplotlib library (for visualization)

## Code Explanation:
This project consists of several key components that work together to solve the maze using a pathfinding algorithm. Below is a detailed explanation of the main functions and variables used in the code.

### Main Components:

#### Maze Representation:
The maze is represented as a 2D list, where:
- 0 indicates an open path.
- 1 indicates a wall.

  For example:<br>
maze = [<br>
    [0, 1, 0, 0, 0],<br>
    [0, 1, 0, 1, 0],<br>
    [0, 0, 0, 1, 0],<br>
    [1, 1, 0, 0, 0],<br>
    [0, 0, 0, 1, 0]<br>
]<br>


#### visualize_maze(maze, path):
* This function visualizes the maze using Matplotlib.
* It displays the maze as a grid where walls and paths are colored differently:
- Walls: Black
- Paths: White
- Solution Path: Red<br><br>

The solution path is drawn as a continuous line that connects the start and goal points. This gives a clear visual representation of the path taken.


#### dfs(maze, start, goal):

* Implements the Depth-First Search (DFS) algorithm to find a path from the start to the goal.
* It uses a stack (LIFO structure) to explore the maze. The algorithm marks cells as visited and backtracks if a dead end is reached.
  
* The process includes:<br>
Base Cases:
1. If the current position is out of bounds or a wall, return None.
2. If the current position is the goal, return the path taken to reach it.<br>
   
Exploration:
1. Add the current position to the path and mark it as visited.
2. Recursively call DFS on adjacent cells (up, down, left, right).<br>
   
Backtracking:
1. If the search does not find a solution, it removes the current position from the path and backtracks to explore other paths.
   
#### solve_maze(maze):
* This function initializes the starting and goal positions and calls the DFS algorithm.
* It stores the resulting path (if found) and calls the visualize_maze function to display the maze and the solution.<br>
  
Example Usage:<br>
To run the maze solver, simply execute:<br>
python maze_solver.py<br>

#### Modify the maze variable in the code to test different maze configurations. The solver will visualize the provided maze and the path found.

#### Key Variables
* start: Tuple indicating the starting position of the maze (usually (0, 0)).
* goal: Tuple indicating the ending position of the maze (e.g., (4, 4)).
* visited: Set that keeps track of visited positions to prevent cycles in the search.<br>

## Result: 

For the following maze:<br><br>
maze= [<br>
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],<br>
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],<br>
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],<br>
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],<br>
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],<br>
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],<br>
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],<br>
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0],<br>
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],<br>
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]<br>
]<br><br>
The output is:<br>
![image](https://github.com/user-attachments/assets/20e6b840-a2a1-434b-8b2f-d0b1762e2f29)

