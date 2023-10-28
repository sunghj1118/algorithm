// DFS

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>

using namespace std;

int N, B;
vector<int> cowHeights;
int minExcessHeight = 1000000000;

void DFS(int index, int currentStackHeight, int totalExcessHeight)
{
    // Cow height finder
    if (index == N)
    {
        if (currentStackHeight >= B)
        {
            minExcessHeight = min(minExcessHeight, totalExcessHeight);
        }
        return;
    }

    // Include current cow in the stack
    int newStackHeight = currentStackHeight + cowHeights[index];
    int newExcessHeight = totalExcessHeight + max(0, newStackHeight - B);
    DFS(index + 1, newStackHeight, newExcessHeight);

    // Skip current cow
    DFS(index + 1, currentStackHeight, totalExcessHeight);
}

int main(void)
{
    // Take input of N and B
    cin >> N >> B;
    cowHeights.resize(N);

    // Take input of all the heights of the cows for N times
    for (int i = 0; i < N; i++)
    {
        cin >> cowHeights[i];
    }

    // Find optimal height of cows. In other words, find the smallest height possible larger than or equal to B.
    DFS(0, 0, 0);

    // Print the answer
    cout << minExcessHeight << endl;
    return 0;
}