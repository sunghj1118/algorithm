# 8958. BAEK Problem Review

## OX퀴즈

### Problem Definition
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

### Approach
- 이거 일단 n을 입력 받고.
- for loop 한번 돌려서 string 계속 입력 받고.
- def OX(s) -> int: 를 만들어서
    - score, temp_score = 0으로 선언
    - for char in s:를 한다.
            - if char == 'O', temp_score +1
            - else, temp_score = 0
        - score = score + temp_score
    - return score

### Solution

```python
def OX(s) -> int:
    score = 0
    temp_score = 0
    for char in s:
        if char == 'O':
            temp_score += 1
        else:
            temp_score = 0
        score += temp_score

    return score


n = int(input())
for i in range(n):
    input_str = str(input())
    print(OX(input_str))

