# main.py

import numpy as np
from dfs_tsp import dfs_tsp
from uniform_cost_tsp import uniform_cost_tsp
from a_star_tsp import a_star_tsp

if __name__ == "__main__":
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])

    # Run DFS
    dfs_path, dfs_cost = dfs_tsp(distances)
    print("DFS Path:", dfs_path)
    print("DFS Cost:", dfs_cost)

    # Run Uniform Cost Search
    ucs_path, ucs_cost = uniform_cost_tsp(distances)
    print("Uniform Cost Path:", ucs_path)
    print("Uniform Cost Cost:", ucs_cost)

    # Run A* Search
    astar_path, astar_cost = a_star_tsp(distances)
    print("A* Path:", astar_path)
    print("A* Cost:", astar_cost)
