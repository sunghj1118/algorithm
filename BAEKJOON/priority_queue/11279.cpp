/*
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
*/

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    int N;

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    priority_queue<int> pq;

    for (int i = 0; i < N; i++)
    {
        int x;
        cin >> x;

        if (x == 0)
        {
            if (pq.empty())
            {
                cout << 0 << "\n";
            }
            else
            {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
        {
            pq.push(x);
        }
    }

    return 0;
}