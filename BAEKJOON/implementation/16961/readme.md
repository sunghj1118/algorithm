# 16961. Problem Review

## 탭 vs 공백

### Problem Definition
큐브러버가 운영하는 호텔은 1년 스케줄을 전년도에 미리 정해놓는다. 또, 이 호텔에는 코딩을 할 줄 아는 사람만 투숙할 수 있다. 코딩을 할 때 들여쓰기는 필수이다. 호텔에는 두 종류의 사람이 투숙하는데, 들여쓰기로 탭을 사용하는 사람과 공백을 사용하는 사람이다. 편의를 위해 각각 "탭파"와 "공백파"로 부르도록 하자.

올해는 윤년이기 때문에, 총 366일로 이루어져 있다. 편의상 날짜는 1일-366일로 표시한다.

큐브러버의 호텔에 예약을 한 사람의 수는 N명이고, 각 사람이 투숙 시작일과 종료일을 모두 알고 있다. 모든 사람은 투숙 시작일의 오전 9시에 호텔에 투숙하고, 투숙 종료일의 오후 6시에 호텔에서 나간다. 이 호텔에는 모든 것이 있기 때문에, 호텔 투숙객은 호텔을 벗어나지 않는다.

탭파와 공백파가 만나면 싸운다. 하지만, 탭파와 공백파의 수가 일치하는 날에는 균형이 잡혀서 싸움이 일어나지 않는다. 탭파가 한 명도 없거나 공백파가 한 명도 없으면 호텔 관리자들끼리 왜 호텔 운영을 이런 식으로 하냐며 서로 책임을 돌리면서 싸운다.

호텔 예약 정보가 주어졌을 때, 여러가지 정보를 구해보려고 한다.

### Approach
어우 길다. 코딩 할줄 아는 사람들만 투숙객으로 받다니 너무하네. 그건 그냥 스타트업이랑 다를게 없지 않나?

아 탭파와 공배파 내용이구나. 윤년에 만들어진 문제면 2020년 또는 2024년이네.

"이 호텔에는 모든 것이 있기 때문에, 호텔 투숙객은 호텔을 벗어나지 않는다." 끔직한데? 진짜 스타트업이잖아.

"탭파와 공백파가 만나면 싸운다. 하지만, 탭파와 공백파의 수가 일치하는 날에는 균형이 잡혀서 싸움이 일어나지 않는다." 강약약강이네.

"탭파가 한 명도 없거나 공백파가 한 명도 없으면 호텔 관리자들끼리 왜 호텔 운영을 이런 식으로 하냐며 서로 책임을 돌리면서 싸운다." 정말 최악이야.

---

와 뭐야 뭐 엄청 많이 시키네.

다음 정보를 한 줄에 하나씩 출력한다.
1. 투숙객이 1명 이상인 날의 수
2. 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
3. 싸움이 없는 날의 수
4. 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수. 싸움이 없는 날이 없으면 0을 출력한다.
5. 가장 오랜 기간 투숙한 사람이 투숙한 날의 수

---
5.가장 오랜 기간 투숙한 사람이 투숙한 날의 수 <br>
그냥 입력을 하나씩 받을 때마다 diff를 계산하여 기존 diff보다 크면 바꾸는 식으로. <br>

1.투숙객이 1명 이상인 날의 수 <br>
- [0] * 366를 먼저 하고.
- for day in range(start_day, end_day+1) 해서 days[day] += 1을 만든다.
- sum of days where guest > 0.

2.가장 많은 투숙객이 있었던 날에 투숙한 사람의 수 <br>
이건 조금 더 쉽다. 그냥 앞서 계산했던거에서 max 찾으면 된다.



### Solution
되는데 왜 틀린지 모르겠다.

생각해보니까 엄청 복잡하게 짰다. 하나의 리스트에 다 때려박았는데, 이걸 tab_count 숙박객들과 space_count 숙박객들로 나누면 좋았을텐데 그렇게 하니까 된다.

```python
n = int(input())
reservations = []

for i in range(n):
    c, s, e = input().split()
    reservations.append([c, int(s)-1, int(e)-1])


days = [[0, 0, 0, 0] for _ in range(366)]  # calendar
e_longest_stay = 0

for reservation in reservations:
    c, s, e = reservation

    # E. Find longest stay
    diff = e - s + 1
    if diff > e_longest_stay:
        e_longest_stay = diff

    for day in range(s, e + 1):
        days[day][0] += 1
        if c == 'T':
            days[day][1] += 1
        if c == 'S':
            days[day][2] += 1

# A. Count days with at least one guest
a_guest_days = sum(1 for day in days if day[0] > 0)
# B. Find the largest amount of guests that stayed in a single night
b_max_day = max(sublist[0] for sublist in days)

# C. Peaceful days
d_max_peace_day = 0
for day in days:
    if (day[1] == 0 or day[2] == 0):  # hotel manager fight
        day[3] = 1
    if (day[1] != day[2]) and (day[1] > 0) and (day[2] > 0):  # tab/space fight
        day[3] = 1
    # D. Find the largest amount of guests that stayed in a night among the peace nights
    if (day[0] > d_max_peace_day):
        d_max_peace_day = day[0]

c_peace_days = sum(1 for day in days if day[3] == 0)
print(a_guest_days)
print(b_max_day)
print(c_peace_days)
print(d_max_peace_day)
print(e_longest_stay)

