// DFS

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>

using namespace std;

const int MAX = 100;
int N, M;
char tiles[MAX][MAX];
bool visited[MAX][MAX];
int cnt = 0;
char now = '-';

void dfs(int i, int j)
{
    // If it is another pattern other than -, or |, return
    if (tiles[i][j] != now)
        return;
    visited[i][j] = true;
    // If is is -, go right
    if (tiles[i][j] == '-')
    {
        if (j + 1 < M)
        {
            if (!visited[i][j + 1])
            {
                dfs(i, j + 1);
            }
        }
    }

    // If it is |, go down
    if (tiles[i][j] == '|')
    {
        if (i + 1 < N)
        {
            if (!visited[i + 1][j])
                dfs(i + 1, j);
        }
    }
}

int main(void)
{
    cin >> N >> M;

    // Input for floor tiles
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> tiles[i][j];
        }
    }

    // Add 1 to cnt every time there is an unvisited plank in the floor
    // traverse for N, M
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            // If current tile hasn't been visited
            if (!visited[i][j])
            {
                visited[i][j] = true;
                cnt++;
                // If current tile is -, and if there exists a next tile to the right that
                // hasn't been visited, go right
                if (tiles[i][j] == '-')
                {
                    if (j + 1 < M)
                    {
                        if (!visited[i][j + 1])
                        {
                            // Change current shape to -
                            now = '-';
                            dfs(i, j + 1);
                        }
                    }
                }

                // If current tile is |, and if there exists a next tile downwards that
                // hasn't been visited, go down
                if (tiles[i][j] == '|')
                {
                    if (i + 1 < N)
                    {
                        if (!visited[i + 1][j])
                        {
                            // Change current shape to |
                            now = '|';
                            dfs(i + 1, j);
                        }
                    }
                }
            }
        }
    }

    cout << cnt << endl;
}