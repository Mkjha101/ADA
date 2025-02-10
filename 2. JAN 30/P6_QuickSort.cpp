#include <iostream>
using namespace std;

// Creating Array of n elements
void CreateArray(int a, int *A){
    srand(time(0));
    for(int i=0; i < a; i++){
        A[i] = rand()%(a+100) + 2;
    }
}

int partition(int* arr, int low, int high) {
    int pivot = arr[high];  // pivot element
    int i = low - 1;

    for(int j = low; j < high; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int* arr, int low, int high) {
    if(low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int n;
    cout << "\t\t\tQuick Sort\n" << "Enter number of elements: ";
    cin >> n;
    int *Array = new int[n];
    CreateArray(n, Array);
    // Sample Array
    cout << "Sample Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;
    quickSort(Array, 0, n - 1);

    cout << "Sorted array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;

    delete[] Array;
    return 0;
}
