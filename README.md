# Traveling Salesman Problem (TSP) Solver

This repository contains implementations of three algorithms to solve the Traveling Salesman Problem (TSP): Depth-First Search (DFS), Uniform Cost Search, and A* Search. The code is organized into separate modules for each algorithm, with a main script to run and compare them.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Code Organization](#code-organization)
4. [Function Descriptions](#function-descriptions)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/tsp-solver.git
    cd tsp-solver
    ```

2. **Install the required packages**:
    The code requires `numpy` for numerical operations. You can install it using pip:
    ```bash
    pip install numpy
    ```

## Usage

1. **Run the main script**:
    The main script `main.py` runs all three algorithms on a predefined distance matrix and compares their results. To execute the script, use:
   
    python main.py

3. **Expected output**:
    The script will print the optimal path and cost for each algorithm:

    DFS Path: [0, 1, 3, 2, 0]
    DFS Cost: 80
    
    Uniform Cost Path: [0, 1, 3, 2, 0]
    Uniform Cost Cost: 80
   
    A* Path: [0, 1, 3, 2, 0]
    A* Cost: 80

## Code Organization

- **`dfs_tsp.py`**: Contains the implementation of the Depth-First Search algorithm for TSP.
- **`uniform_cost_tsp.py`**: Contains the implementation of the Uniform Cost Search algorithm for TSP.
- **`a_star_tsp.py`**: Contains the implementation of the A* Search algorithm for TSP with a simple heuristic.
- **`main.py`**: Main script to run and compare the results of all three algorithms.

## Function Descriptions

### Module: `dfs_tsp.py`
1. **Function**: `dfs_tsp(distances)`
   - **Description**: Implements the Depth-First Search algorithm to find the optimal TSP path.
   - **Parameters**:
   - `distances`: A 2D numpy array representing the distance matrix.
   - **Return Value**: A tuple `(min_path, min_cost)` where `min_path` is the optimal path and `min_cost` is the cost of this path.

### Module: `uniform_cost_tsp.py`
1. **Function**: `uniform_cost_tsp(distances)`
   - **Description**: Implements the Uniform Cost Search algorithm to find the optimal TSP path.
   - **Parameters**:
     - `distances`: A 2D numpy array representing the distance matrix.
   - **Return Value**: A tuple `(min_path, min_cost)` where `min_path` is the optimal path and `min_cost` is the cost of this path.

### Module: `a_star_tsp.py`
1. **Function**: `simple_heuristic(distances, current_city, unvisited)`
   - **Description**: Simple heuristic function that returns 0, acting as a baseline.
   - **Parameters**:
     - `distances`: A 2D numpy array representing the distance matrix.
     - `current_city`: The current city being considered.
     - `unvisited`: A set of cities that have not yet been visited.
   - **Return Value**: An integer heuristic value (0 in this case).

2. **Function**: `a_star_tsp(distances)`
   - **Description**: Implements the A* Search algorithm to find the optimal TSP path.
   - **Parameters**:
     - `distances`: A 2D numpy array representing the distance matrix.
   - **Return Value**: A tuple `(min_path, min_cost)` where `min_path` is the optimal path and `min_cost` is the cost of this path.

### Module: `main.py`
1. **Function**: `main()`
   - **Description**: Main script to run and compare the results of all three algorithms.
   - **Parameters**: None
   - **Return Value**: None (prints the paths and costs of the three algorithms).

