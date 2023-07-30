/*
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
*/

#include <iostream>
#include <queue>

using namespace std;

int N, K;
int visited[100001];
queue<pair<int, int>> q;

int BFS(int N, int K)
{
    visited[N] = 1;
    q.push(make_pair(N, 0));

    while (!q.empty())
    {
        int current_position = q.front().first;
        int time = q.front().second;
        q.pop();

        if (current_position == K)
        {
            return time;
        }

        // 걷는 경우
        if (current_position - 1 >= 0 && !visited[current_position - 1])
        {
            q.push(make_pair(current_position - 1, time + 1));
            visited[current_position - 1] = 1;
        }
        if (current_position + 1 <= 100000 && !visited[current_position + 1])
        {
            q.push(make_pair(current_position + 1, time + 1));
            visited[current_position + 1] = 1;
        }

        // 순간이동 하는 경우
        if (current_position * 2 <= 100000 && !visited[current_position * 2])
        {
            q.push(make_pair(current_position * 2, time + 1));
            visited[current_position * 2] = 1;
        }
    }

    // 동생을 찾지 못한 경우
    return -1;
}

int main()
{
    cin >> N >> K;
    cout << BFS(N, K) << endl;
}