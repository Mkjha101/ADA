#include <iostream>
#include <vector>
using namespace std;

// Function to find the index of the maximum element in a given column
int findMaxIndex(const vector<vector<int>>& matrix, int col, int rows) {
    int max_row = 0;
    for (int i = 1; i < rows; i++) {
        if (matrix[i][col] > matrix[max_row][col])
            max_row = i;
    }
    return max_row;
}

// Function to find a peak element using Divide and Conquer
pair<int, int> find2DPeak(const vector<vector<int>>& matrix, int cols, int rows, int start_col, int end_col) {
    int mid_col = start_col + (end_col - start_col) / 2;
    int max_row = findMaxIndex(matrix, mid_col, rows);

    // Check if the mid_col element is a peak
    int current = matrix[max_row][mid_col];
    int left = (mid_col - 1 >= 0) ? matrix[max_row][mid_col - 1] : -1;
    int right = (mid_col + 1 < cols) ? matrix[max_row][mid_col + 1] : -1;

    if (current >= left && current >= right) {
        return {max_row, mid_col};  // Peak found
    }
    else if (left > current) {
        return find2DPeak(matrix, cols, rows, start_col, mid_col - 1);
    }
    else {
        return find2DPeak(matrix, cols, rows, mid_col + 1, end_col);
    }
}

int main() {
    vector<vector<int>> matrix = {
        {10, 8, 10, 10},
        {14, 13, 12, 11},
        {15, 9, 11, 21},
        {16, 17, 19, 20}
    };

    int rows = matrix.size();
    int cols = matrix[0].size();

    pair<int, int> peak = find2DPeak(matrix, cols, rows, 0, cols - 1);
    cout << "Peak element is " << matrix[peak.first][peak.second]
         << " at position (" << peak.first << ", " << peak.second << ")" << endl;

    return 0;
}
