# 11729. Problem Review

## 11729. Hanoi Tower

### Problem Definition
하노이 탑 문제.

한번쯤 들어봤을거다. 재귀를 사용해서 탑을 옮겨야 하는 문제.

https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

### Approach
큰 규칙은 다음과 같다:

1) N-1개의 판을 C를 사용하여, A에서 B로 옮긴다.
2) 가장 큰 판을 A에서 C로 옮긴다.
3) A를 사용하여 나머지 N-1 판들을 B에서 C로 옮긴다.

알고리즘:
- towerOfHanoi(current_num_of_disk, from_rod, to_rod, aux_rod) 함수를 만들어라
- N-1th 판을 위한 함수를 호출
- 현재 판을 출력
- N-1th 판을 다시 한번 호출

### Solution
- 키포인트1: global 선언 해야 내부 함수에서 1 증가.
- 출력 순서 지키기 위해 list에 저장.

```python
count = 0
steps = []


def towerOfHanoi(n, from_rod, to_rod, aux_rod):  # n = current_num_of_disk
    global count
    if n == 0:
        return
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    count += 1
    steps.append(str(from_rod) + " " + str(to_rod))
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)


N = int(input())

towerOfHanoi(N, 1, 3, 2)
print(count)
for step in steps:
    print(step)

```