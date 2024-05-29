# uniform_cost_tsp.py

import numpy as np
import heapq

def uniform_cost_tsp(distances):
    num_cities = len(distances)
    pq = [(0, 0, [0])]
    min_cost = float('inf')
    min_path = []

    while pq:
        cost, current_city, path = heapq.heappop(pq)
        if len(path) == num_cities and distances[current_city][0] > 0:
            total_cost = cost + distances[current_city][0]
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = path + [0]
            continue

        for i in range(num_cities):
            if i not in path and distances[current_city][i] > 0:
                heapq.heappush(pq, (cost + distances[current_city][i], i, path + [i]))

    return min_path, min_cost

if __name__ == "__main__":
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    path, cost = uniform_cost_tsp(distances)
    print("Uniform Cost Path:", path)
    print("Uniform Cost Cost:", cost)
