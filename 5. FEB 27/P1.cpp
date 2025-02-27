#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Activity {
    int start, end;
};

bool compare(Activity a1, Activity a2) {
    return a1.end < a2.end;
}

void selectActivities(vector<Activity>& activities) {
    sort(activities.begin(), activities.end(), compare);

    cout << "Selected Activities (start, end):\n";
    int lastEnd = -1;
    for (auto act : activities) {
        if (act.start >= lastEnd) {
            cout << "(" << act.start << ", " << act.end << ")\n";
            lastEnd = act.end;
        }
    }
}

int main() {
    int n;
    cout << "Enter number of activities: ";
    cin >> n;

    vector<Activity> activities(n);
    cout << "Enter start and end time for each activity:\n";
    for (int i = 0; i < n; i++) {
        cin >> activities[i].start >> activities[i].end;
    }

    selectActivities(activities);
    return 0;
}
