from tsp.utils import calculate_distance, generate_initial_solution
import random

def local_search(distance_matrix, max_iterations=1000, verbose=False):
    """
    Perform Local Search for the Traveling Salesman Problem.
    """
    num_cities = len(distance_matrix)
    current_solution = generate_initial_solution(num_cities)
    current_distance = calculate_distance(current_solution, distance_matrix)
    
    for iteration in range(max_iterations):
        city1, city2 = random.sample(range(num_cities), 2)
        neighbor_solution = current_solution[:]
        neighbor_solution[city1], neighbor_solution[city2] = neighbor_solution[city2], neighbor_solution[city1]
        neighbor_distance = calculate_distance(neighbor_solution, distance_matrix)
        
        if neighbor_distance < current_distance:
            current_solution = neighbor_solution
            current_distance = neighbor_distance
        
        if verbose:
            print(f"Iteration {iteration}: Current Distance = {current_distance}")
    
    return current_solution, current_distance