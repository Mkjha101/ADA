#include <iostream>
using namespace std;

// Function to calculate area of triangle
float area(int x1, int y1, int x2, int y2, int x3, int y3) {
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0);
}

// Function to check if point (x, y) lies inside triangle
bool isInside(int x1, int y1, int x2, int y2, int x3, int y3, int x, int y) {
    float A = area(x1, y1, x2, y2, x3, y3);
    float A1 = area(x, y, x2, y2, x3, y3);
    float A2 = area(x1, y1, x, y, x3, y3);
    float A3 = area(x1, y1, x2, y2, x, y);

    return (A == A1 + A2 + A3);
}

int main() {
    int x1, y1, x2, y2, x3, y3, x, y;
    cout << "Enter triangle vertices:\n";
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    cout << "Enter point to test:\n";
    cin >> x >> y;

    if (isInside(x1, y1, x2, y2, x3, y3, x, y))
        cout << "Point lies inside the triangle.\n";
    else
        cout << "Point lies outside the triangle.\n";

    return 0;
}
