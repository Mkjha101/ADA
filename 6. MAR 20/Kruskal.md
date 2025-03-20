# Kruskal's Algorithm

## Aim:
To find the Minimum Spanning Tree (MST) of a connected, undirected graph using Kruskal's Algorithm.

## Time Complexity:
O(E log E), where E is the number of edges (due to sorting).

## Algorithm:
1. Sort all the edges by weight.
2. Use a disjoint set to detect cycles.
3. Pick the smallest edge that doesn’t form a cycle.
4. Repeat until MST contains (V-1) edges.

## Applications:
- Network design (electrical, computer, road networks)
- Approximation algorithms for NP-hard problems like TSP

## 📤 Output Image
![Output](OUTPUT%20IMAGES/P1.png "1D Peak Output")

## 📈 Graph
![Time Complexity](OUTPUT%20IMAGES/P1_Graph.png "Not Available")
