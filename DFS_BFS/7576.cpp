#include <iostream>
#include <queue>

using namespace std;
#define MAX 1001

int N, M, days = 0;      // 토마토 농장 넓이 및 소요 시간
int tomato[MAX][MAX];    // 인접 행렬 그래프
bool visited[MAX][MAX];  // 정점 방문 여부
queue<pair<int, int>> q; // 탐색 좌표 저장

int x_dir[4] = {-1, 1, 0, 0}; // x축 상하좌우
int y_dir[4] = {0, 0, -1, 1}; // y축 상하좌우

void BFS()
{
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int x_new = x + x_dir[i];
            int y_new = y + y_dir[i];

            if ((0 <= x_new && x_new < N) && (0 <= y_new && y_new < M) && tomato[x_new][y_new] == 1)
            {
                tomato[x_new][y_new] = tomato[x][y] + 1;
                q.push(make_pair(x_new, y_new));
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
            scanf("%1d", &tomato[i][j]);
            if (tomato[i][j] == 1)
            {
                q.push({i, j});
            }
        }
    }

    BFS();

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            // 익지않은 토마토(0)가 존재할 경우
            if (tomato[i][j] == 0)
            {
                printf("-1\n");
                return 0;
            }
            // 토마토는 다 익었는데, 얼마만에 익었는지?
            if (days < tomato[i][j])
            {
                days = tomato[i][j];
            }
        }
    }

    cout << days - 1;
}