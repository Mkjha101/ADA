#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int u, v, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};

int find(vector<int>& parent, int u) {
    if (u != parent[u])
        parent[u] = find(parent, parent[u]);
    return parent[u];
}

void unite(vector<int>& parent, vector<int>& rank, int u, int v) {
    u = find(parent, u);
    v = find(parent, v);
    if (u != v) {
        if (rank[u] < rank[v])
            swap(u, v);
        parent[v] = u;
        if (rank[u] == rank[v])
            rank[u]++;
    }
}

int main() {
    int n = 6; // number of vertices
    vector<Edge> edges = {
        {0, 1, 4}, {0, 2, 4}, {1, 2, 2}, {1, 3, 5},
        {2, 3, 8}, {2, 4, 10}, {3, 4, 2}, {3, 5, 6}, {4, 5, 3}
    };

    sort(edges.begin(), edges.end());
    vector<int> parent(n), rank(n, 0);
    for (int i = 0; i < n; i++) parent[i] = i;

    vector<Edge> mst;
    int cost = 0;

    for (Edge e : edges) {
        if (find(parent, e.u) != find(parent, e.v)) {
            mst.push_back(e);
            cost += e.weight;
            unite(parent, rank, e.u, e.v);
        }
    }

    cout << "Edges in MST:\n";
    for (Edge e : mst)
        cout << e.u << " - " << e.v << " : " << e.weight << "\n";
    cout << "Total cost: " << cost << "\n";
}
