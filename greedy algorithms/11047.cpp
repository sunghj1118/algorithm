#include <iostream>

using namespace std;

int coins[11];
int main() {
    int n, k;

    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    int i = n - 1;
    int count=0;
    while (i>=0) {
        count += k / coins[i];
        k = k % coins[i];
        i--;
    }
    cout << count << endl;
}