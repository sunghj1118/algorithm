#include <iostream>
#include <queue>

using namespace std;
#define MAX 1001

int N, M, ans;     // 컴퓨터 수, 연결 수, 감염 컴퓨터 수
int map[MAX][MAX]; // 인접 행렬 그래프
bool visited[MAX]; // 정점 방문 여부
queue<int> q;      // 탐색 좌표 저장

void BFS()
{
    visited[1] = true;
    q.push(1);

    while (!q.empty())
    {
        int x;
        x = q.front();
        q.pop();
        for (int i = 1; i <= N; i++)
        {
            if (visited[i] == 0 && map[x][i] == 1)
            {
                q.push(i);
                visited[i] = true;
                ans++;
            }
        }
    }
}

int main()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
        map[b][a] = 1;
    }

    BFS();

    cout << ans;
}