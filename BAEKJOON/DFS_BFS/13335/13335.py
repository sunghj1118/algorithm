from collections import deque

# 첫줄 입력 값을 받는다
n, b, w = map(int, input().split())  # 트럭 수 n, 다리 길이 b, 최대하중 w

# 트럭 수만큼 큐에 입력한다
trucks = deque(map(int, input().split()))


def least_time_taken(queue):
    # 소요된 시간, 다리 위 하중
    time_taken = 0
    current_weight = 0
    bridge = deque([0]*b, maxlen=b)

    while queue or sum(bridge) > 0:
        # 시간이 간다
        time_taken += 1

        # 다리 위에 트럭이 있다면, 첫번째 트럭이 도착했는지 확인
        # 만약 그렇다면, 다리에서 삭제
        current_weight -= bridge.popleft()

        # 다리의 하중에 아직 여유가 있고, 다리에 공간이 있다면
        if trucks and (current_weight + trucks[0]) <= w and queue:
            truck = queue.popleft()
            current_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)

    return time_taken


print(least_time_taken(trucks))
