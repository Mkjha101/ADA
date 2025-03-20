import time
import random
import matplotlib.pyplot as mp
import math
import heapq

# Prim's Algorithm using Min-Heap (Priority Queue)
def prims_algorithm(graph, V):
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, vertex)
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    return total_cost

# Graph generation
def generate_graph(V, max_weight=100):
    graph = [[] for _ in range(V)]
    for u in range(V):
        for v in range(u + 1, V):
            weight = random.randint(1, max_weight)
            graph[u].append((v, weight))
            graph[v].append((u, weight))  # undirected graph
    return graph

# Time complexity graph plot
def run_and_plot():
    sizes = list(range(100, 1001, 100))
    times = []

    for V in sizes:
        graph = generate_graph(V)
        start = time.perf_counter()
        prims_algorithm(graph, V)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # in milliseconds

    # Expected Time Complexity ~ O(V^2) or O(E log V) with priority queue
    scale_factor = times[0] / (sizes[0] ** 2)
    expected_curve = [scale_factor * (n ** 2) for n in sizes]

    # Plotting the graph
    mp.plot(sizes, times, label="Actual Time", marker='o', color='blue')
    mp.plot(sizes, expected_curve, label="Expected ~ V²", linestyle='--', color='red')

    mp.xlabel("Number of Vertices (V)")
    mp.ylabel("Execution Time (ms)")
    mp.title("Time Complexity of Prim's Algorithm")
    mp.legend()
    mp.grid(True)
    mp.tight_layout()
    mp.show()

run_and_plot()
