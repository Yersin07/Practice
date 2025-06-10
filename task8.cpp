#include<iostream>
using namespace std;
int main() {
    int W;
    float H;
    cin >> W;
    cin >> H;
    cout << "Your BMI is " << W / (H * H);
    return 0;
}