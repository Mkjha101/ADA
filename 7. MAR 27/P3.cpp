#include <iostream>
#include <vector>
#include <queue>
#include<climits>
using namespace std;

#define N 12

void computeStages(int graph[N][N], int source, vector<int> &stage) {
    stage.assign(N, -1);
    queue<int> q;

    stage[source] = 0; // Source is at stage 0
    q.push(source);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < N; v++) {
            if (graph[u][v] != INT_MAX && stage[v] == -1) {
                stage[v] = stage[u] + 1;
                q.push(v);
            }
        }
    }

    // Output the stages
    cout << "Stages of nodes:\n";
    for (int i = 0; i < N; i++) {
        cout << "Node " << i << " is in stage " << stage[i] << endl;
    }
}

int main() {
    int graph[N][N] = {
        {INT_MAX, 7 , 3 , 1 , 4 ,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 8 , 4 ,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 6 , 10,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 2 , 11,INT_MAX,INT_MAX,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 4 ,INT_MAX,INT_MAX,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 8 ,INT_MAX,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 14, 13,INT_MAX,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 12, 6 ,INT_MAX},
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 4 },
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 7 },
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX, 9 },
        {INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX,INT_MAX}
    };

    vector<int> stage;
    computeStages(graph, 0, stage);

    return 0;
}