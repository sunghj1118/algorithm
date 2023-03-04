#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 1000;
int coins[MAX];

int main() {
    int n, k;

    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    int i = n - 1;
    int count=0;
    while (k > 0) {
        if (coins[i] < k) {
            count += k / coins[i];
            k = k % coins[i];
            i--;
        }
        else {
            i--;
        }
    }
    cout << count << endl;
}