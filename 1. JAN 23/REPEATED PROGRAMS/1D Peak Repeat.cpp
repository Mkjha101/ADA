#include <iostream>
using namespace std;

// Function to find a peak element
int findPeak(int arr[], int low, int high, int n) {
    int mid = low + (high - low) / 2;

    // Check if mid is a peak
    if ((mid == 0 || arr[mid - 1] <= arr[mid]) &&
        (mid == n - 1 || arr[mid + 1] <= arr[mid]))
        return mid;

    // If left neighbor is greater, recurse on left half
    if (mid > 0 && arr[mid - 1] > arr[mid])
        return findPeak(arr, low, mid - 1, n);

    // Else recurse on right half
    return findPeak(arr, mid + 1, high, n);
}

int main() {
    int arr[] = {1, 3, 20, 4, 1, 0};
    int n = sizeof(arr) / sizeof(arr[0]);

    int peakIndex = findPeak(arr, 0, n - 1, n);
    cout << "Peak element is " << arr[peakIndex] << " at index " << peakIndex << endl;

    return 0;
}
