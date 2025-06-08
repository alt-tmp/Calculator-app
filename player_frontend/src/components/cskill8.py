from collections import deque

# Function to print the steps to reach the target
def print_solution(path):
    print("Steps to reach the goal:")
    for state in path:
        print(f"Jug A: {state[0]}, Jug B: {state[1]}")
    
# Function to solve the Water Jug Problem using BFS
def water_jug_bfs(a, b, target):
    # Initial state: both jugs are empty
    visited = set()
    queue = deque([((0, 0), [])])  # (jug_a, jug_b), path

    while queue:
        (jug_a, jug_b), path = queue.popleft()

        # Add current state to the path
        path.append((jug_a, jug_b))

        # Check if the target is reached
        if jug_a == target or jug_b == target:
            print_solution(path)
            return True

        # Skip if the state is already visited
        if (jug_a, jug_b) in visited:
            continue

        # Mark the state as visited
        visited.add((jug_a, jug_b))

        # Possible moves
        possible_moves = [
            (a, jug_b),  # Fill Jug A
            (jug_a, b),  # Fill Jug B
            (0, jug_b),  # Empty Jug A
            (jug_a, 0),  # Empty Jug B
            # Pour Jug A -> Jug B
            (jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)),
            # Pour Jug B -> Jug A
            (jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a))
        ]

        # Add all possible next states to the queue
        for next_state in possible_moves:
            if next_state not in visited:
                queue.append((next_state, path.copy()))

    print("No solution found.")
    return False

# Input values
if __name__ == "__main__":
    jug_a_capacity = int(input("Enter capacity of Jug A: "))
    jug_b_capacity = int(input("Enter capacity of Jug B: "))
    target_amount = int(input("Enter target amount: "))

    # Call the BFS function
    water_jug_bfs(jug_a_capacity, jug_b_capacity, target_amount)
    print("Vedant")