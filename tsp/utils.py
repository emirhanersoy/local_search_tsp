import random
import math

def calculate_euclidean_distance(coord1, coord2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def generate_distance_matrix(coordinates):
    """
    Generate a symmetric distance matrix from a list of coordinates.
    """
    num_cities = len(coordinates)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = calculate_euclidean_distance(coordinates[i], coordinates[j])
    
    return distance_matrix

def generate_initial_solution(num_cities):
    """
    Generate a random initial solution (route) for the TSP problem.
    """
    route = list(range(num_cities))
    random.shuffle(route)
    return route

def calculate_distance(route, distance_matrix):
    """
    Calculate the total distance of a given route using the distance matrix.
    """
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance_matrix[route[i]][route[(i + 1) % len(route)]]
    return total_distance