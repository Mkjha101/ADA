#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int value, weight;
    double ratio;

    Item(int v, int w) {
        value = v;
        weight = w;
        ratio = (double)v / w;
    }
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int capacity, vector<Item>& items) {
    sort(items.begin(), items.end(), compare);

    double totalValue = 0.0;

    for (auto& item : items) {
        if (capacity >= item.weight) {
            capacity -= item.weight;
            totalValue += item.value;
        } else {
            totalValue += item.ratio * capacity;
            break;
        }
    }

    return totalValue;
}

int main() {
    int n, capacity;
    cout << "Enter number of items: ";
    cin >> n;

    vector<Item> items;
    cout << "Enter value and weight of each item:\n";
    for (int i = 0; i < n; ++i) {
        int v, w;
        cin >> v >> w;
        items.emplace_back(v, w);
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    double maxValue = fractionalKnapsack(capacity, items);
    cout << "Maximum value in knapsack = " << maxValue << endl;

    return 0;
}
