// Program for 1D Peak
#include <iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter number of elements: ";
    cin>>n;

    // Creating Array of n elements and an array for finding Peaks
    int Array[n],Peak[n];
    for(int i=0; i<n; i++){
        cin >> Array[i];
        Peak[i]=0;
    }

    // Finding Peaks in given 1-Dimensional array
    for(int i=0; i<n; i++){
        if(i>0 && i<n-1)
            if(Array[i]>Array[i-1] && Array[i]>Array[i+1])
                Peak[i]=1;

        if((i==0) && (Array[i]>Array[i+1]))
            Peak[i]=1;
            
        if(i==n-1)
            if(Array[i]>Array[i-1])
                Peak[i]=1;
    }

    // Output
    cout << "\n" << "Peak Array is: " << "[";
    for(int i=0; i<n; i++){
        cout << Peak[i];
        if(i!=n-1){
            cout << ",";            
        }
    }
    cout << "]";

    return 0;
}