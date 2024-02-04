from collections import deque


q = deque()
visited = [0] * 100001


def BFS(N, K):
    q.append([N, 0])

    while q:
        visited[N] = 1
        cur = q.popleft()
        current_position, time = cur[0], cur[1]

        # 찾았을 경우
        if current_position == K:
            return time

        # 걷는 경우
        if (current_position - 1 >= 0 and visited[current_position-1] == 0):
            q.append([current_position-1, time+1])
            visited[current_position-1] = 1
        if (current_position + 1 <= 100000 and visited[current_position+1] == 0):
            q.append([current_position+1, time+1])
            visited[current_position+1] = 1

        # 순간이동
        if (current_position * 2 <= 100000 and visited[current_position*2] == 0):
            q.append([current_position*2, time+1])
            visited[current_position*2] = 1

    return -1


N, K = map(int, input().split())

print(BFS(N, K))
