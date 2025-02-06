// --Aim: Calculating a^b in O(log n) time complexity using Divide and Conquer.

#include <iostream>
using namespace std;

// Function to compute a^b using Divide and Conquer (Exponentiation by Squaring)
long long power(long long a, long long b) {
    if (b == 0)
        return 1;
    long long half = power(a, b / 2);
    if (b % 2 == 0)
        return half * half;
    else
        return a * half * half;
}

int main() {
    long long a, b;
    cout << "Enter base (a): ";
    cin >> a;
    cout << "Enter exponent (b): ";
    cin >> b;
    cout << a << "^" << b << " = " << power(a, b) << endl;
    return 0;
}
