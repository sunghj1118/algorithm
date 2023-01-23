#include <iostream>
using namespace std;

long long dist[100000];
long long cityprice[100000];

int main() {
    
    long long total, current;

    // taking inputs
    long long ncities = 0;
    cin >> ncities;

    for (int i = 0; i < ncities - 1; i++) {
        cin >> dist[i];
    }
    for (int i = 0; i < ncities; i++) {
        cin >> cityprice[i];
    }

    // first move
    total = dist[0] * cityprice[0];
    current = cityprice[0];

    // comparing prices (starting at i = 1 since the first step is a must)
    for (int i = 1; i < ncities; i++)
    {
        if (current < cityprice[i]) { //our current is cheaper than the next city
            total += current * dist[i];
        }
        else { //if the next city is cheaper, we must buy to go to the next city.
            current = cityprice[i];
            total += current * dist[i];
        }
    }

    cout << total;
}