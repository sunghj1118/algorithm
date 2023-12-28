#include <iostream>
using namespace std;

int main() {
    int N, M, temp;
    N = M = temp = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        temp = i;
        M = temp;
        while (temp > 0) {
            M = M + temp % 10;
            temp = temp / 10;
        }

        if (M == N) {
            cout << i << endl;
            return 0;
        }
    }
    cout << 0 << endl;
}