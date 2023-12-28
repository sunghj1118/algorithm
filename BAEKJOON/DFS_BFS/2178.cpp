#include <iostream>
#include <queue>

using namespace std;
#define MAX 1001

int N, M;                // 미로 크기
int maze[MAX][MAX];      // 인접 행렬 그래프
bool visited[MAX][MAX];  // 정점 방문 여부
queue<pair<int, int>> q; // 탐색 좌표 저장

int x_dir[4] = {-1, 1, 0, 0}; // x축 상하좌우
int y_dir[4] = {0, 0, -1, 1}; // y축 상하좌우
int dist[MAX][MAX];

void BFS()
{
    visited[0][0] = 1; // 시작좌표
    q.push(make_pair(0, 0));
    dist[0][0] = 1;

    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;

        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int x_new = x + x_dir[i];
            int y_new = y + y_dir[i];

            if ((0 <= x_new && x_new < N) && (0 <= y_new && y_new < M) && !visited[x_new][y_new] && maze[x_new][y_new] == 1)
            {
                visited[x_new][y_new] = 1;
                q.push(make_pair(x_new, y_new));
                dist[x_new][y_new] = dist[x][y] + 1;
            }
        }
    }
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%1d", &maze[i][j]);
        }
    }

    BFS();

    cout << dist[N - 1][M - 1];
}