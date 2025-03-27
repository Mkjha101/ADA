import time
import matplotlib.pyplot as plt
import numpy as np

def shortest_distance(graph, N):
    dist = [float('inf')] * N
    next_node = [-1] * N
    dist[N - 1] = 0  # Sink node distance = 0

    for i in range(N - 2, -1, -1):
        for j in range(i + 1, N):
            if graph[i][j] != np.inf and graph[i][j] + dist[j] < dist[i]:
                dist[i] = graph[i][j] + dist[j]
                next_node[i] = j

    return dist[0], next_node

def measure_runtime(max_N=100, step=5):
    N_values = range(10, max_N + 1, step)
    runtimes = []

    for N in N_values:
        # Generate a random DAG (upper triangular matrix)
        graph = np.random.randint(1, 100, size=(N, N))
        graph = np.triu(graph, k=1)  # Ensure strict DAG (no diagonal)
        graph = graph.astype(float)  # Convert to float to support infinity
        graph[graph == 0] = np.inf  # No edge = INF

        start_time = time.time()
        shortest_distance(graph, N)
        end_time = time.time()
        runtimes.append((end_time - start_time) * 1000)  # Convert to milliseconds

    return N_values, runtimes

def plot_complexity(N_values, runtimes):
    plt.figure(figsize=(10, 6))
    
    # Plot actual runtime (teal)
    plt.plot(N_values, runtimes, 'o-', color='teal', label='Actual Runtime (ms)')
    
    # Plot theoretical O(N²) complexity (crimson)
    theoretical = [ (N ** 2) * 0.001 for N in N_values ]  # Scaling factor
    plt.plot(N_values, theoretical, '--', color='crimson', label='O(N²) Complexity (Scaled)')
    
    plt.xlabel('Number of Nodes (N)')
    plt.ylabel('Time (milliseconds)')
    plt.title('Time Complexity of Shortest Path in DAG (DP Approach)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run analysis
N_values, runtimes = measure_runtime()
plot_complexity(N_values, runtimes)