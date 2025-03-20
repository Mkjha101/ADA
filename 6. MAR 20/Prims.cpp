#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> P;

void primMST(vector<vector<P>>& graph, int V) {
    priority_queue<P, vector<P>, greater<P>> pq;
    vector<int> key(V, INT_MAX);
    vector<bool> inMST(V, false);
    vector<int> parent(V, -1);

    pq.push({0, 0});
    key[0] = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        inMST[u] = true;

        for (auto [v, weight] : graph[u]) {
            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                pq.push({key[v], v});
                parent[v] = u;
            }
        }
    }

    cout << "Edges in MST:\n";
    for (int i = 1; i < V; i++)
        cout << parent[i] << " - " << i << " : " << key[i] << "\n";
}

int main() {
    int V = 6;
    vector<vector<P>> graph(V);

    graph[0].push_back({1, 4});
    graph[0].push_back({2, 4});
    graph[1].push_back({2, 2});
    graph[1].push_back({3, 5});
    graph[2].push_back({3, 8});
    graph[2].push_back({4, 10});
    graph[3].push_back({4, 2});
    graph[3].push_back({5, 6});
    graph[4].push_back({5, 3});

    primMST(graph, V);
}
