from queue import PriorityQueue

# Define the size of the grid
N = 9

# Directions for moving in 4 possible directions (up, down, left, right)
ROW_DIRECTIONS = [-1, 1, 0, 0]
COL_DIRECTIONS = [0, 0, -1, 1]

# Check if cell is valid, within bounds, and not blocked
def is_valid(row, col):
    return 0 <= row < N and 0 <= col < N

# Heuristic function: Manhattan distance
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# A* search algorithm
def a_star_search(grid, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        # Check if we have reached the goal
        if current == goal:
            break

        # Explore neighbors
        for i in range(4):
            new_row = current[0] + ROW_DIRECTIONS[i]
            new_col = current[1] + COL_DIRECTIONS[i]

            if is_valid(new_row, new_col) and grid[new_row][new_col] == 0:
                new_cost = cost_so_far[current] + 1

                # Check if this path is better
                if (new_row, new_col) not in cost_so_far or new_cost < cost_so_far[(new_row, new_col)]:
                    cost_so_far[(new_row, new_col)] = new_cost
                    priority = new_cost + heuristic(new_row, new_col, goal[0], goal[1])
                    open_list.put((priority, (new_row, new_col)))
                    came_from[(new_row, new_col)] = current

    return came_from, cost_so_far

# Reconstruct the path from goal to start
def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Main function to define grid and run A* algorithm
if __name__ == "__main__":
    # Define the grid (0 = free cell, 1 = obstacle)
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start = (8, 0)  # Starting position
    goal = (0, 0)  # Goal position

    # Run A* search
    came_from, cost_so_far = a_star_search(grid, start, goal)

    # Check if a path was found
    if goal in came_from:
        print("The destination cell is found")
        path = reconstruct_path(came_from, start, goal)
        print("The Path is")
        print(" -> ".join(str(cell) for cell in path))
    else:
        print("No path found")

    # Print the name after execution
    print("\nVedant")