# 11656. Problem Review

## 11656. 접미사 배열

### Problem Definition
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

### Approach
- s가 존재하지 않을 때까지 하나씩 줄여서 리스트에 추가하고 sort.

### Solution
- solved. key: make sure that there are no empty values in list.

```python
s = str(input())
jubmisa = [s]

while s:
    s = s[1:]
    jubmisa.append(s)

jubmisa = [value for value in jubmisa if value]

jubmisa.sort()

for value in jubmisa:
    print(value)

```