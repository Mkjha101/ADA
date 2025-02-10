#include <iostream>
using namespace std;

// Creating Array of n elements
void CreateArray(int a, int *A){
    srand(time(0));
    for(int i=0; i < a; i++){
        A[i] = rand()%(a+100) + 2;
    }
}

void heapify(int* arr, int n, int i) {
    int largest = i;       // Initialize largest as root
    int left = 2 * i + 1;  // left child
    int right = 2 * i + 2; // right child

    if(left < n && arr[left] > arr[largest])
        largest = left;

    if(right < n && arr[right] > arr[largest])
        largest = right;

    if(largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest); // Recursively heapify the affected sub-tree
    }
}

void heapSort(int* arr, int n) {
    // Build max heap
    for(int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract elements
    for(int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    int n;
    cout << "\t\t\tHeap Sort\n" << "Enter number of elements: ";
    cin >> n;
    int *Array = new int[n];
    CreateArray(n, Array);
    // Sample Array
    cout << "Sample Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;
    heapSort(Array, n);

    cout << "\nSorted array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;

    delete[] Array;
    return 0;
}
