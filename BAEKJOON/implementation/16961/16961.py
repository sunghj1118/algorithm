N = int(input())  # 투숙객 수
stays = [input().split() for _ in range(N)]

# 날짜별 탭파와 공백파 수를 기록할 배열
tab_count = [0] * 367
space_count = [0] * 367

# 투숙 정보를 기반으로 탭파와 공백파 수 계산
for stay in stays:
    c, s, e = stay[0], int(stay[1]), int(stay[2])
    for day in range(s, e + 1):
        if c == 'T':
            tab_count[day] += 1
        else:
            space_count[day] += 1

# 필요한 정보 계산
days_with_guests = sum(1 for i in range(
    1, 367) if tab_count[i] + space_count[i] > 0)
max_guests = max(tab_count[i] + space_count[i] for i in range(1, 367))
peaceful_days = sum(1 for i in range(
    1, 367) if tab_count[i] == space_count[i] and tab_count[i] > 0)
# 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날의 투숙객 수 계산
guests_on_peaceful_days = []
for i in range(1, 367):
    if tab_count[i] == space_count[i] and tab_count[i] > 0:
        guests_on_peaceful_days.append(tab_count[i] + space_count[i])

max_guests_peaceful = max(guests_on_peaceful_days, default=0)
# 가장 오랜 기간 투숙한 사람의 투숙 일수 계산
longest_stay_duration = 0
for stay in stays:
    c, start, end = stay[0], int(stay[1]), int(stay[2])
    stay_duration = end - start + 1
    if stay_duration > longest_stay_duration:
        longest_stay_duration = stay_duration

longest_stay = longest_stay_duration

# 출력
print(days_with_guests)
print(max_guests)
print(peaceful_days)
print(max_guests_peaceful)
print(longest_stay)
