import heapq
import random
import time
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    V = len(graph)
    dist = [float('inf')] * V
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

def generate_graph(n, edges_per_node=3):
    graph = [[] for _ in range(n)]
    for u in range(n):
        for _ in range(edges_per_node):
            v = random.randint(0, n - 1)
            if u != v:
                w = random.randint(1, 10)
                graph[u].append((v, w))
    return graph

input_sizes = [100 * i for i in range(1, 11)]
actual_times = []

for n in input_sizes:
    G = generate_graph(n)
    start_time = time.time()
    dijkstra(G, 0)
    end_time = time.time()
    actual_times.append(end_time - start_time)

expected_times = [x * actual_times[-1] / input_sizes[-1] * (1 + 0.1) for x in input_sizes]  # Roughly O((V+E) log V)

plt.plot(input_sizes, actual_times, 'o-', color='teal', label='Actual Time')
plt.plot(input_sizes, expected_times, 'r--', label='Expected Time O((V+E) log V)')
plt.xlabel("Number of Vertices")
plt.ylabel("Time (s)")
plt.title("Dijkstra's Algorithm Time Complexity")
plt.grid(True)
plt.legend()
plt.show()
