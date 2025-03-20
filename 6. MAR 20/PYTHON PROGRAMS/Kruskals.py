class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[u_root] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, w))
            total_cost += w
            ds.union(u, v)

    return mst, total_cost

n = 6
edges = [
    (0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 3, 5),
    (2, 3, 8), (2, 4, 10), (3, 4, 2), (3, 5, 6), (4, 5, 3)
]

mst, cost = kruskal(n, edges)
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")
print("Total cost:", cost)
