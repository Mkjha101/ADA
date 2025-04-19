//  Program for 2-Dimensionl Peak
#include <iostream>
using namespace std;
int main(){
    // Creating Test Array
    int n,m;
    cout << "Enter number of rows: ";
    cin >> m;
    cout << "Enter number of columns: ";
    cin >> n;
    int Arr[m][n], Peaks[m][n];
    cout << "\nEnter Elements\n";

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin >> Arr[i][j];
            Peaks[i][j]=0;
        }
    }

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
            if(i==n-1){
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
            if(i>0 && i<n-1){
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
            count==1?Peaks[i][j]=1:0;

            /*
            // New Approach
            if(Arr[i][j]>Arr[i][j+1] && Arr[i][j]>Arr[i][j-1] && Arr[i][j]>Arr[i-1][j] && Arr[i][j]>Arr[i+1][j]){
                Peaks[i][j]=1;
            }
            cout << "i: " << i << "\tj: " << j << "\tPeaks: " << Peaks[i][j] << endl;
            */
        }
    }

    // Printing answer
    cout << "\nPeaks are at following positions:-\n";
    for(int i=0; i<m; i++){
        cout << "[";
        for(int j=0; j<n; j++){
            cout << Peaks[i][j];
            if(j!=n-1){
                cout << ", ";
            }
        }
        cout << "]\n";
    }
    return 0;
}