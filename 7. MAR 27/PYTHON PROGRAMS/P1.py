import time
import matplotlib.pyplot as plt
import numpy as np

def knapsack_solver(n, W):
    # Worst-case: All items have weight=1 and high value (forcing full DP computation)
    items = [(1, 100)] * n  # Each item has weight=1, maximizing DP computations
    
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i-1][0] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][0]] + items[i-1][1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

def measure_worst_case_runtime():
    n_values = range(10, 201, 10)  # Number of items (n)
    W = 100  # Fixed capacity (W)
    runtimes = []
    
    for n in n_values:
        start_time = time.time()
        knapsack_solver(n, W)
        end_time = time.time()
        runtimes.append((end_time - start_time) * 1000)  # Convert to milliseconds
    
    return n_values, runtimes

def plot_worst_case_complexity(n_values, runtimes):
    plt.figure(figsize=(10, 6))
    
    # Plot actual runtime (teal)
    plt.plot(n_values, runtimes, 'o-', color='teal', label='Actual Runtime (ms)')
    
    # Plot theoretical O(n*W) complexity (crimson)
    theoretical = np.array(n_values) * 0.01  # Scaling factor for visualization
    plt.plot(n_values, theoretical, '--', color='crimson', label='O(n*W) Complexity (Scaled)')
    
    plt.xlabel('Number of Items (n)')
    plt.ylabel('Time (milliseconds)')
    plt.title('Worst-Case Time Complexity of 0/1 Knapsack (W=100)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run analysis
n_values, runtimes = measure_worst_case_runtime()
plot_worst_case_complexity(n_values, runtimes)