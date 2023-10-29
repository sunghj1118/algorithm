// DFS

#include <iostream>
#include <queue>

using namespace std;

int N;
int arr[3][3];

string bfs()
{
    queue<pair<int, int>> q;
    q.push({0, 0});

    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        int step = arr[x][y];
        q.pop();

        if (step == -1)
            return "HaruHaru";
        if (step == 0)
            continue;

        if (x + step < N)
            q.push({x + step, y});
        if (y + step < N)
            q.push({x, y + step});
    }

    return "Hing";
}

int main()
{
    cin >> N;

    // for grid size N, take input for N * N grid
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> arr[i][j];
        }
    }
    cout << bfs() << endl;
}
