#include <iostream>
using namespace std;

int main() {
    int l, p, v, days, left_days;
    int count = 0;
    while(1)
    {
        cin >> l >> p >> v;
        if (l == 0 && p == 0 && v == 0) {
            break;
        }

        days = (v / p) * l;
        left_days = v % p;
        if (left_days > l) {
            days += l;
        }
        else {
            days += left_days;
        }

        count++;
        cout << "Case " << count << ": " << days << "\n";
    }
}