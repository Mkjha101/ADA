#include<iostream>
#include<algorithm>
#include<ctime>
using namespace std;

int main() {
    srand(static_cast<unsigned>(time(0)));
    int capacity = rand() % 10 + 10; 

    int** items = new int*[5];
    for (int i = 0; i < 5; ++i) {
        items[i] = new int[2]; 
    }
    // Assign weights and values
    for (int i = 0; i < 5; ++i) {
        items[i][0] = rand() % 10 + 1; // weight
        items[i][1] = rand() % 100;    // value
    }
    // Displaying the items
    cout << "Item List (Weight, Value):\n";
    for (int i = 0; i < 5; ++i) {
        cout << "Item " << i + 1 << ": (" << items[i][0] << ", " << items[i][1] << ")\n";
    }
    cout << "Knapsack Capacity: " << capacity << "\n";

    int** dp = new int*[6];
    for (int i = 0; i <= 5; ++i) {
        dp[i] = new int[capacity + 1]();
    }
    // filling in the dp
    for (int i = 1; i <= 5; ++i) {
        for (int j = 1; j <= capacity; ++j) {
            if (j >= items[i - 1][0]) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][0]] + items[i - 1][1]);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << "Maximum Achievable Profit: " << dp[5][capacity] << "\n";

    int w = capacity;
    cout << "Selected Items (Weight, Value):\n";
    for (int i = 5; i > 0 && w > 0; --i) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << "Item " << i << ": (" << items[i - 1][0] << ", " << items[i - 1][1] << ")\n";
            w -= items[i - 1][0];
        }
    }

    // Deleting memory allocation
    for (int i = 0; i < 5; ++i) {
        delete[] items[i];
    }
    delete[] items;
    for (int i = 0; i <= 5; ++i) {
        delete[] dp[i];
    }
    delete[] dp;

    return 0;
}