#include <iostream>
using namespace std;

// fixed amount of coins
int coins[11];

int main() {
    // taking input n amount of coins and k money to calculate
    int n, k;
    cin >> n >> k;

    // taking input of coins
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    int count=0;
    for(int i=n-1; i>=0; i--){
        // adding how many coins fit into our money to the count
        count += k/coins[i];
    
        // taking out the amount we used for our coins counted
        k = k%coins[i];
    }
    
    // printing min amount of coins
    cout << count << endl;
}