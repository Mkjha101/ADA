#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
using namespace std;

// Creating Array of n elements
void CreateArray(int a, int *A){
    srand(time(0));
    for(int i=0; i < a; i++){
        A[i] = rand()%(a+100) + 2;
    }
}

void selectionSort(int * arr, int n) {
    for(int i = 0; i < n-1; i++) {
        int minIndex = i;
        for(int j = i+1; j < n; j++) {
            if(arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if(minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
}

int main() {
    int n;
    cout << "\t\t\tSelection Sort\n" << "Enter number of elements: ";
    cin >> n;
    int *Array = new int[n];
        CreateArray(n, Array);
    // Sample Array
    cout << "Sample Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;
        selectionSort(Array, n);

    // Printing Sorted Array
    cout << "\nSorted Array:\n";
    for(int i = 0; i < n; i++) {
        cout << Array[i] << " ";
    }
    cout << endl;

    return 0;
}
