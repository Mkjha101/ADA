#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

struct Point {
    int x, y;
};

Point p0;

int orientation(Point a, Point b, Point c) {
    int val = (b.y - a.y)*(c.x - b.x) - (b.x - a.x)*(c.y - b.y);
    if (val == 0) return 0;  // collinear
    return (val > 0) ? 1 : 2; // clock or counterclock wise
}

int distSq(Point a, Point b) {
    return (a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y);
}

bool compare(Point a, Point b) {
    int o = orientation(p0, a, b);
    if (o == 0)
        return distSq(p0, a) < distSq(p0, b);
    return o == 2;
}

void convexHull(vector<Point>& points) {
    int n = points.size();
    if (n < 3) return;

    int ymin = points[0].y, min_idx = 0;
    for (int i = 1; i < n; i++) {
        if ((points[i].y < ymin) || (points[i].y == ymin && points[i].x < points[min_idx].x)) {
            ymin = points[i].y;
            min_idx = i;
        }
    }

    swap(points[0], points[min_idx]);
    p0 = points[0];

    sort(points.begin() + 1, points.end(), compare);

    stack<Point> hull;
    hull.push(points[0]);
    hull.push(points[1]);
    hull.push(points[2]);

    for (int i = 3; i < n; i++) {
        while (hull.size() > 1) {
            Point top = hull.top(); hull.pop();
            Point nextToTop = hull.top();
            if (orientation(nextToTop, top, points[i]) != 2)
                continue;
            else {
                hull.push(top);
                break;
            }
        }
        hull.push(points[i]);
    }

    cout << "Points in Convex Hull:\n";
    while (!hull.empty()) {
        Point p = hull.top(); hull.pop();
        cout << "(" << p.x << ", " << p.y << ")\n";
    }
}

int main() {
    int n;
    cout << "Enter number of points: ";
    cin >> n;

    vector<Point> points(n);
    cout << "Enter x and y coordinates:\n";
    for (int i = 0; i < n; i++)
        cin >> points[i].x >> points[i].y;

    convexHull(points);
    return 0;
}
