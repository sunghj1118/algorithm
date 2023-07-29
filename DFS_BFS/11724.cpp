// 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

#include <iostream>

using namespace std;

int N, M, cnt = 0;     // 정점 개수, 간선 개수, 연결 요소 개수
int graph[1001][1001]; // 인접 행렬 그래프
bool visited[1001];    // 정점 방문 여부

void DFS(int v)
{
    visited[v] = true;

    for (int i = 1; i <= N; i++)
    {
        if (graph[v][i] == 1 && visited[i] == false)
        {
            DFS(i);
        }
    }
}

int main()
{
    cin >> N >> M;

    // 인접 행렬 그래프 초기화
    for (int i = 0; i < M; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u][v] = graph[v][u] = 1;
    }

    // DFS
    for (int i = 1; i <= N; i++)
    {
        if (visited[i] == false)
        {
            DFS(i);
            cnt++;
        }
    }

    cout << cnt << endl;
}