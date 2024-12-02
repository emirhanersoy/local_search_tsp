from tsp.utils import generate_distance_matrix
from tsp.search import local_search
from tsp.plot import plot_solution

if __name__ == "__main__":
    # Örnek şehir koordinatları
    coordinates = [(0, 0), (2, 3), (5, 5), (8, 2), (6, 7)]
    
    # Mesafe matrisi oluştur
    distance_matrix = generate_distance_matrix(coordinates)
    
    # Local Search uygulaması
    solution, total_distance = local_search(distance_matrix, max_iterations=100)
    
    # Sonuçları yazdır
    print("En iyi rota:", solution)
    print("Toplam mesafe:", total_distance)
    
    # Çözümü görselleştir
    plot_solution(coordinates, solution)