import matplotlib.pyplot as plt

def plot_solution(coordinates, route):
    """
    Plot the TSP solution on a 2D graph.
    """
    x = [coordinates[city][0] for city in route] + [coordinates[route[0]][0]]
    y = [coordinates[city][1] for city in route] + [coordinates[route[0]][1]]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("Traveling Salesman Problem Solution")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()