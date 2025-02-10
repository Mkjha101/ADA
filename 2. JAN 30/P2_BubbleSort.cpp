#include <iostream>
using namespace std;

// Creating Array of n elements
void CreateArray(int a, int *A){
    srand(time(0));
    for(int i=0; i < a; i++){
        A[i] = rand()%(a+100) + 2;
    }
}

void bubbleSort(int* arr, int n) {
    for(int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for(int j = 0; j < n - i - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if(!swapped) break; // Optimization: stop if already sorted
    }
}

int main() {
    int n;
    cout << "\t\t\tBubble Sort\n" << "Enter number of elements: ";
    cin >> n;
    int *Array = new int[n];
    CreateArray(n, Array);
    // Sample Array
    cout << "Sample Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;
    bubbleSort(Array, n);

    cout << "\nSorted Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;

    delete[] Array; // free the memory
    return 0;
}
