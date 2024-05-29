# a_star_tsp.py

import numpy as np
import heapq

def simple_heuristic(distances, current_city, unvisited):
    """Heuristic: Return 0 as a baseline."""
    return 0

def a_star_tsp(distances):
    num_cities = len(distances)
    pq = [(0, 0, [0], set(range(1, num_cities)))]
    min_cost = float('inf')
    min_path = []

    while pq:
        cost, current_city, path, unvisited = heapq.heappop(pq)
        if not unvisited:
            total_cost = cost + distances[current_city][0]
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = path + [0]
            continue

        for i in unvisited:
            new_cost = cost + distances[current_city][i]
            heuristic_cost = new_cost + simple_heuristic(distances, i, unvisited - {i})
            heapq.heappush(pq, (heuristic_cost, i, path + [i], unvisited - {i}))

    return min_path, min_cost

# Example usage
if __name__ == "__main__":
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    path, cost = a_star_tsp(distances)
    print("A* Path:", path)
    print("A* Cost:", cost)
