import math
import random

# Objective function to minimize (can be modified as needed)
def objective_function(x):
    return x[0] ** 2 + x[1] ** 2 + 5 * math.sin(x[0]) * math.cos(x[1])

# Simulated Annealing Algorithm
def simulated_annealing(objective_function, bounds, initial_temp, final_temp, alpha, max_iter):
    # Generate initial solution within the bounds
    current_solution = [random.uniform(bounds[0], bounds[1]) for _ in range(2)]
    best_solution = list(current_solution)
    current_evaluation = objective_function(current_solution)
    best_evaluation = current_evaluation

    temp = initial_temp
    iteration = 0

    # Simulated annealing loop
    while temp > final_temp and iteration <= max_iter:
        # Generate new candidate solution by tweaking current solution
        new_solution = [current_solution[i] + random.uniform(-0.1, 0.1) for i in range(2)]
        
        # Clip the solution within bounds
        new_solution = [max(bounds[0], min(bounds[1], new_solution[i])) for i in range(2)]
        new_evaluation = objective_function(new_solution)

        # Accept the new solution if it is better or probabilistically
        if new_evaluation < current_evaluation or random.random() < math.exp((current_evaluation - new_evaluation) / temp):
            current_solution = list(new_solution)
            current_evaluation = new_evaluation

        # Update the best solution if the new one is better
        if current_evaluation < best_evaluation:
            best_solution = list(current_solution)
            best_evaluation = current_evaluation

        # Print iteration info every 100 iterations
        if iteration % 100 == 0:
            print(f"Iteration {iteration}, Temperature {temp:.3f}, Best Evaluation {best_evaluation:.5f}")

        # Reduce the temperature
        temp *= alpha
        iteration += 1

    return best_solution, best_evaluation

# Main function to set parameters and run the algorithm
if __name__ == "__main__":
    # Define search space boundaries
    bounds = [-5, 5]  # Range for variables
    initial_temp = 10.0  # Initial temperature
    final_temp = 0.01  # Minimum temperature
    alpha = 0.95  # Cooling rate
    max_iter = 900  # Number of iterations

    # Run simulated annealing
    best_solution, best_score = simulated_annealing(objective_function, bounds, initial_temp, final_temp, alpha, max_iter)

    # Print the best solution and score after completion
    print(f"\nBest Solution: {best_solution}")
    print(f"Best Score: {best_score:.5f}")

    # Print name at the end
    print("\nVedant")