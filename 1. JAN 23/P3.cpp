#include <iostream>
#include <vector>
using namespace std;

// Function to generate an odd-order magic square
vector<vector<int>> generateMagicSquare(int n) {
    vector<vector<int>> magicSquare(n, vector<int>(n, 0));

    int num = 1;
    int i = 0, j = n / 2;

    while (num <= n * n) {
        magicSquare[i][j] = num;
        num++;
        int new_i = (i - 1 + n) % n;
        int new_j = (j + 1) % n;

        if (magicSquare[new_i][new_j] != 0) {
            i = (i + 1) % n;
        } else {
            i = new_i;
            j = new_j;
        }
    }

    return magicSquare;
}

int main() {
    int n;
    cout << "Enter an odd number (n): ";
    cin >> n;

    if (n % 2 == 0) {
        cout << "Only odd-order magic squares are supported using this method.\n";
        return 1;
    }

    vector<vector<int>> magicSquare = generateMagicSquare(n);

    cout << "Magic Square of size " << n << ":\n";
    for (auto& row : magicSquare) {
        for (int val : row)
            cout << val << "\t";
        cout << endl;
    }

    return 0;
}
