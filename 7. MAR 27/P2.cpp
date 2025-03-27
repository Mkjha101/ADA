#include <iostream>
#include <vector>
#include <climits>
using namespace std;

#define N 12
#define INF INT_MAX

void ShortestDistance(int graph[N][N]) {
    vector<int> dist(N, INF);
    vector<int> next(N, -1);  
    dist[N - 1] = 0; 

    for (int i = N - 2; i >= 0; i--) {
        for (int j = i + 1; j < N; j++) {
            if (graph[i][j] != INF && graph[i][j] + dist[j] < dist[i]) {
                dist[i] = graph[i][j] + dist[j];
                next[i] = j;  
            }
        }
    }

    cout << "\nMinimum distance from source (0) to sink (" << N - 1 << ") = " << dist[0] << endl;

    cout << "Path followed: ";
    int current = 0;
    while (current != -1) {
        cout << current;
        if (next[current] != -1) cout << " -> ";
        current = next[current];
    }
    cout << endl;
}

int main() {
    int grap[12][12] = {
        {INF, 7 , 3 , 1 , 4 ,INF,INF,INF,INF,INF,INF,INF},
        {INF,INF,INF,INF,INF, 8 , 4 ,INF,INF,INF,INF,INF},
        {INF,INF,INF,INF,INF, 6 , 10,INF,INF,INF,INF,INF},
        {INF,INF,INF,INF,INF,INF, 2 , 11,INF,INF,INF,INF},
        {INF,INF,INF,INF,INF,INF,INF, 4 ,INF,INF,INF,INF},
        {INF,INF,INF,INF,INF,INF,INF,INF, 8 ,INF,INF,INF},
        {INF,INF,INF,INF,INF,INF,INF,INF, 14, 13,INF,INF},
        {INF,INF,INF,INF,INF,INF,INF,INF,INF, 12, 6 ,INF},
        {INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF, 4 },
        {INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF, 7 },
        {INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF, 9 },
        {INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF}
    };

    ShortestDistance(grap);
    return 0;
}