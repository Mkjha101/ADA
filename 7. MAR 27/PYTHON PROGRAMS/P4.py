import time
import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

def total_cost(mask, curr, n, cost, memo):
    if mask == (1 << n) - 1:
        return cost[curr][0]
    if memo[curr][mask] != -1:
        return memo[curr][mask]
    
    ans = float('inf')
    for i in range(n):
        if not (mask & (1 << i)):
            new_cost = cost[curr][i] + total_cost(mask | (1 << i), i, n, cost, memo)
            ans = min(ans, new_cost)
    memo[curr][mask] = ans
    return ans

def tsp(cost):
    n = len(cost)
    memo = [[-1] * (1 << n) for _ in range(n)]
    return total_cost(1, 0, n, cost, memo)

def measure_tsp_runtime(max_n=12):
    n_values = range(2, max_n + 1)
    runtimes = []
    
    for n in n_values:
        # Generate a random symmetric cost matrix
        np.random.seed(42)
        cost_matrix = np.random.randint(1, 100, size=(n, n))
        cost_matrix = (cost_matrix + cost_matrix.T) // 2  # Make symmetric
        np.fill_diagonal(cost_matrix, 0)  # Diagonal = 0
        
        start_time = time.time()
        tsp(cost_matrix)
        end_time = time.time()
        runtimes.append((end_time - start_time) * 1000)  # Convert to milliseconds
    
    return n_values, runtimes

def plot_tsp_complexity(n_values, runtimes):
    plt.figure(figsize=(10, 6))
    
    # Plot actual runtime (teal)
    plt.plot(n_values, runtimes, 'o-', color='teal', label='Actual Runtime (ms)')
    
    # Plot theoretical O(n² * 2ⁿ) complexity (crimson)
    theoretical = [ (n ** 2) * (2 ** n) * 0.000001 for n in n_values ]  # Scaling factor
    plt.plot(n_values, theoretical, '--', color='crimson', label='O(n² × 2ⁿ) Complexity (Scaled)')
    
    plt.xlabel('Number of Cities (n)')
    plt.ylabel('Time (milliseconds)')
    plt.title('Worst-Case Time Complexity of TSP (DP + Memoization)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run analysis
n_values, runtimes = measure_tsp_runtime()
plot_tsp_complexity(n_values, runtimes)