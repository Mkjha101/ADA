//  Program for 2-Dimensionl Peak
#include <iostream>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()
using namespace std;

void Array(int** Arr, int** P, int m, int n) {
    srand(time(0)); // Seed for randomness
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            Arr[i][j] = rand() % (m + n + 1);
            P[i][j]=0;
        }
    }
}

void Peaks(int m, int n, int** Arr, int** Peaks){
    // Testing for Peaks
    /*
        For any element at any place in the matrix,
        if its value is greater than all of its neighbours,
        then that position is one of the Peaks.
    */
   for(int i=0; i<m; i++){
    for(int j=0; j<n; j++){
        int count=0;
        
        // For the first Array
        if(i==0){
            if(j==0){
                if(Arr[i][j]>Arr[i+1][j] && Arr[i][j]>Arr[i][j+1]){
                    count=1;
                }
            }
            else if(j==(n-1)){
                (Arr[i][j]>Arr[i+1][j] && Arr[i][j]>Arr[i][j-1])?(count=1):0;
            }
            else{
                if(Arr[i][j]>Arr[i][j-1] && Arr[i][j]>Arr[i][j+1] && Arr[i][j]>Arr[i+1][j]){
                    count=1;
                }
            }
        }
        
        // For the last Array
        if(i==m-1){
            if(j==0){
                if(Arr[i][j]>Arr[i-1][j] && Arr[i][j]>Arr[i][j+1]){
                    count=1;
                }
            }
            else if(j==(n-1)){
                (Arr[i][j]>Arr[i-1][j] && Arr[i][j]>Arr[i][j-1])?(count=1):0;
            }
            else{
                if(Arr[i][j]>Arr[i][j-1] && Arr[i][j]>Arr[i][j+1] && Arr[i][j]>Arr[i-1][j]){
                    count=1;
                }
            }
        }

        // For other Arrays
        if(i>0 && i<m-1){
            if(j==0){
                (Arr[i][j]>Arr[i][j+1] && Arr[i][j]>Arr[i+1][j] && Arr[i][j]>Arr[i-1][j])?count=1:0;
            }
            else if(j==n-1){
                (Arr[i][j]>Arr[i][j-1] && Arr[i][j]>Arr[i+1][j] && Arr[i][j]>Arr[i-1][j])?count=1:0;
            }
            else{
                (Arr[i][j]>Arr[i][j-1] && Arr[i][j]>Arr[i][j+1] && Arr[i][j]>Arr[i+1][j] && Arr[i][j]>Arr[i-1][j])?count=1:0;
            }
        }
        if(count==1)
            Peaks[i][j]=1;
    }
}

}
int main(){
    int m,n;
    cout << "Enter number of rows: ";
    cin >> m;
    cout << "Enter number of columns: ";
    cin >> n;

    int** Arr = new int *[m];
    int** Peak = new int *[m];
    for(int i=0; i<m; i++){
        Arr[i] = new int[n];
        Peak[i] = new int[n];
    }
    // Creating Arrays
    Array(Arr, Peak, m, n);
    /*
    cout << "\nEnter Elements\n";
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cout << "Enter element (" << i+1 << "," << j+1 << "): ";
            cin >> Arr[i][j];
            Peak[i][j] = 0;
        }
        cout << endl;
    }
        */
    // Peaks
    Peaks(m, n, Arr, Peak);
    
    // Printing Object Matrix
    cout << "\nGiven Matrix:-\n";
    for(int i=0; i<m; i++){
        cout << "[";
        for(int j=0; j<n; j++){
            cout << Arr[i][j];
            if(j!=n-1){
                cout << ", ";
            }
        }
        cout << "]\n";
    }

    // Printing answer
    cout << "\nPeaks are at following positions:-\n";
    for(int i=0; i<m; i++){
        cout << "[";
        for(int j=0; j<n; j++){
            cout << Peak[i][j];
            if(j!=n-1){
                cout << ", ";
            }
        }
        cout << "]\n";
    }
    return 0;
}