#include <iostream>
using namespace std;

// Creating Array of n elements
void CreateArray(int a, int *A){
    srand(time(0));
    for(int i=0; i < a; i++){
        A[i] = rand()%(a+100) + 2;
    }
}

void insertionSort(int* arr, int n) {
    for(int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1] greater than key to one position ahead
        while(j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

int main() {
    int n;
    cout << "\t\t\tInsertion Sort\n" << "Enter number of elements: ";
    cin >> n;
    int *Array = new int[n];
    CreateArray(n, Array);
    // Sample Array
    cout << "Sample Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;
    insertionSort(Array, n);

    cout << "Sorted array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;
    delete[] Array;
    return 0;
}
