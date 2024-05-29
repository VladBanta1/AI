# dfs_tsp.py

import numpy as np

def dfs_tsp(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    min_path = []
    min_cost = float('inf')

    def dfs(current_city, count, cost, path):
        nonlocal min_cost, min_path
        if count == num_cities and distances[current_city][0] > 0:
            total_cost = cost + distances[current_city][0]
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = path + [0]
            return

        for i in range(num_cities):
            if not visited[i] and distances[current_city][i] > 0:
                visited[i] = True
                dfs(i, count + 1, cost + distances[current_city][i], path + [i])
                visited[i] = False

    visited[0] = True
    dfs(0, 1, 0, [0])
    return min_path, min_cost

if __name__ == "__main__":
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    path, cost = dfs_tsp(distances)
    print("DFS Path:", path)
    print("DFS Cost:", cost)
