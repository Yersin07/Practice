#include<iostream>
using namespace std;
int main() {
    int P, R, T;
    cin >> P;
    cin >> R;
    cin >> T;
    cout << "Simple interest is " << (P * R * T) / 100;
    return 0;
}