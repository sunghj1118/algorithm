import sys
input = sys.stdin.readline

def dfs(x,y,visited, depth):
    global max_distance
    max_distance = max(max_distance, depth)

    n = board[x][y]
    visited[ord(n) - 65] = True
    adj_list = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    check = 0

    # 상하좌우로 이동
    for point in adj_list:
        px, py = point[0], point[1]

        # 보드 범위 내에 있고, 아직 방문하지 않은 알파벳인 경우
        if 0 <= px < R and 0 <= py < C:
            n = board[px][py]
            if visited[ord(n)-65] == False:
                check += 1
                dfs(px,py,visited, depth+1)
                visited[ord(n)-65] = False

R,C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [False for x in range(26)]

max_distance = 0

# start at 0,0
dfs(0,0, visited, 1)

print(max_distance)