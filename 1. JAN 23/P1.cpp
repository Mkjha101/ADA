// Program for 1D Peak
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <iomanip>
#include <vector>  // For dynamic storage
using namespace std;
using namespace std::chrono;

// Creating Array of n elements
void CreateArray(int a, int *A, int *P){
    srand(time(0));
    for(int i=0; i < a; i++){
        A[i] = rand()%(a+100);
        P[i] = 0;
    }
}
// Finding Peaks
nanoseconds Peaks(int n, int *A, int *P){
    auto start = high_resolution_clock::now();
    for(int i=0; i<n; i++){
        if(i>0 && i<n-1)
            if(*A>*(A+1) && *A>*(A-1))
                *P=1;
        else if((i==0) && (*A>*(A+1)))
            *P=1;
        if(i==n-1 && *A>*(A-1))
                *P=1;
        A++; P++;
    }
    auto end = high_resolution_clock::now();
    auto duration= duration_cast<nanoseconds>(end-start);
    //cout << "Time Taken by code: " << duration.count() << " nanoseconds" << endl;
    return duration;
}

int main(){
    int n = 500;
    float m;
    cout << "Enter Multiplier: "; cin >> m;
    if(m==0 || m==1){
        m=1.5;
    }

    // Vector to store observations and timings
    vector<int> Obs;
    vector<double> T;
    while(n<100000){
        int *Array = new int[n],*Peak = new int[n];
        CreateArray(n, Array, Peak);
        nanoseconds Time = nanoseconds::zero();
        for(int i=0; i < 100; i++){
            Time += Peaks(n, &Array[0], &Peak[0]);
        }
        auto Average = Time/100;
        double seconds = Average.count()/1e9; // Converting nanoseconds to seconds.
        cout << "For n = "<<n<< ", Average Time = "<<seconds<< fixed << setprecision(9) <<" seconds"<<endl;
        delete [] Array;
        delete [] Peak;
        // Store Results
        Obs.push_back(n);
        T.push_back(seconds);
        n*=m;
    }
    
    // Output in case of 1 Observation
    /*
    cout << "\n" << "Peak Array is: " << "[";
    for(int i=0; i<n; i++){
        cout << Peak[i];
        if(i!=n-1){
            cout << ",";            
        }
    }
    cout << "]";
    */

    // Output arrays for plotting
    cout << "\n\n// Data for Plotting" << endl;
    cout << "Observations = [";
    for(size_t i = 0; i < Obs.size(); i++){
        cout << Obs[i];
        if(i != Obs.size()-1) cout << ", ";
    }
    cout << "]" << endl;

    cout << "Time_values = [";
    for(size_t i = 0; i < T.size(); i++){
        cout << T[i];
        if(i != T.size()-1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}