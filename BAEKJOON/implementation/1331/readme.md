# 1331. Problem Review

## 나이트 투어 / 기사 순회공연

### Problem Definition
    나이트 투어는 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며, 마지막으로 방문하는 칸에서 시작점으로 돌아올 수 있는 경로이다. 다음 그림은 나이트 투어의 한 예이다.

    영식이는 6×6 체스판 위에서 또 다른 나이트 투어의 경로를 찾으려고 한다. 체스판의 한 칸은 A, B, C, D, E, F 중에서 하나와 1, 2, 3, 4, 5, 6 중에서 하나를 이어 붙인 것으로 나타낼 수 있다. 영식이의 나이트 투어 경로가 주어질 때, 이것이 올바른 것이면 Valid, 올바르지 않으면 Invalid를 출력하는 프로그램을 작성하시오.

Q. 뭐만 하면 붙히는게 '구현' 태그인 것 같다. Implementation이 정확히 뭐길래. 그냥 어떤 알고리즘을 써도 결국에 구현이지 않은가? 나는 아직도 구현 문제가 왜 개별적인 태그인지 이해가 가질 않는다. 특별한 알고리즘 없이 어떻게든 푸는거라고 한다면 하드 코딩과의 차이도 정확히 이해가 가질 않는다.

C. 그와 별개로 이 Knight Tour 문제는 뭔가 딱 봐도 무조건 풀어야 하는 문제 같은 느낌이다. Keystone 문제 느낌.

### Approach
Q. 기사가 모든 타일을 정확히 한번씩 밟는다는건 이해가 되는데, 돌아올때도 모든 타일을 밟아야 하는가?<br>
A. 일단 36개의 입력을 받는걸 보아하니 돌아오는건 생각 안해도 되는것 같다. (6x6 그리드/즉 모든 타일)

- 그렇다면 이걸 구현하기 위해서는 우리는 현재 칸에서 우리 말이 어디 칸으로 갈 수 있는지 알려줘야 한다. 느낌상 recursion(재귀)를 써야 하는것 같다.
- 하나의 칸에서 다음 갈 수 있는 4개의 후보들으로 함수를 재귀 호출해서 가고, visited인지 표시를 해야 한다.
- 그렇게 갈 수 있는 모든 경로들을 가다 보면 표현 가능한 모든 경로가 아마 나올것이다.
- 그러나, 우리의 문제는 모든 경로가 아닌, 현재 경로가 유효한지만 보면 되는거다 보니, 여러 탈락 조건만 살펴보면 된다.
    - **갈 수 없는 칸을 입력 받았을 때.** 현재 칸에서 갈 수 있는 위치는 4개지만 그 중 해당하지 않는걸 입력 받았을 경우 바로 Return Invalid.
    - **이미 가본 칸을 다시 호출 할 때.**
- 이 두개만 한다면 얼추 될 것 같다.

- 체스보드에서 가능한 위치를 어떻게 하지? 아. 알파벳이 들어가서 좀 복잡하게 생각했던거지 그냥 6x6에서 위치만 2개, 1개 조정하면 되겠구나.

### Solution
**Attempt 1**:
- 내 시도는 다음과 같았다. 첫 위치에 제대로 도착할 수 있는 고려하지 않아서 틀렸었다.

```python

def check(prev, next, visited):
    """Check if pos is visited and if it is possible to move to pos"""
    # need to check if visited
    if visited[next[0]][next[1]]:
        return False

    # need to check if possible to move
    if abs(prev[0] - next[0]) == 2 and abs(prev[1] - next[1]) == 1:
        return True
    elif abs(prev[0] - next[0]) == 1 and abs(prev[1] - next[1]) == 2:
        return True
    else:
        return False


def translate(pos):
    """Translates chess language position to index
    translate chess language to index
    ex) A1 -> (0, 0), B1 -> (0, 1), A2 -> (1, 0), ...
    """
    letter = pos[0]
    num = int(pos[1])

    mapping = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5
    }

    if letter in mapping:
        return (num - 1, mapping[letter])
    else:
        return (-1, -1)


# input
visited = [[False] * 6 for _ in range(6)]
prev = (0, 0)

for i in range(1, 36):
    pos = input()
    pos = translate(pos)

    if i == 1:  # first input
        visited[pos[0]][pos[1]] = True
        prev = pos
        pass
    elif check(prev, pos, visited):  # check if possible to move
        visited[pos[0]][pos[1]] = True
        prev = pos
    else:
        print("Invalid")
        break

print("Valid")
```

**Attempt 2**:
- 46% 정도까지 올라갔다가 틀렸다고 나온다. 예제에 있는건 다 맞게 출력한다.
- 보니까 모든 칸을 다 방문했는지 구현을 안했었다.

```python

def check(prev, next, visited):
    """Check if pos is visited and if it is possible to move to pos"""
    # need to check if visited
    if visited[next[0]][next[1]]:
        return False

    # need to check if possible to move
    if abs(prev[0] - next[0]) == 2 and abs(prev[1] - next[1]) == 1:
        return True
    elif abs(prev[0] - next[0]) == 1 and abs(prev[1] - next[1]) == 2:
        return True
    else:
        return False


def translate(pos):
    """Translates chess language position to index
    translate chess language to index
    ex) A1 -> (0, 0), B1 -> (0, 1), A2 -> (1, 0), ...
    """
    letter = pos[0]
    num = int(pos[1])

    mapping = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5
    }

    if letter in mapping:
        return (num - 1, mapping[letter])
    else:
        return (-1, -1)


# input
visited = [[False] * 6 for _ in range(6)]
first_pos = (0, 0)
prev = (0, 0)
flag = True

for i in range(36):
    pos = input()
    pos = translate(pos)

    if i == 0:  # first input
        first_pos = pos
        prev = pos
        pass
    elif i == 35:  # last input
        # need to check if possible to move to first position
        if abs(pos[0] - first_pos[0]) == 2 and abs(pos[1] - first_pos[1]) == 1:
            visited[pos[0]][pos[1]] = True
            visited[first_pos[0]][first_pos[1]] = True
            pass
        elif abs(pos[0] - first_pos[0]) == 1 and abs(pos[1] - first_pos[1]) == 2:
            visited[pos[0]][pos[1]] = True
            visited[first_pos[0]][first_pos[1]] = True
            pass
        else:
            print("Invalid")
            flag = False
            break
    elif check(prev, pos, visited):  # check if possible to move
        visited[pos[0]][pos[1]] = True
        prev = pos
    else:
        print("Invalid")
        flag = False
        break

if flag:
    # check if all positions are visited
    for i in range(6):
        for j in range(6):
            if not visited[i][j]:
                print("Invalid")
                flag = False
                break
    print("Valid")
```

위와 같이 짰다.


**Attempt 3**:

그래도 안되고 같은 46%에서 틀린다. 왜일까? 마지막 출력하는걸 바꾸니까 해결됐다.

다음과 같이 바꾸니까 해결됐다. 아마 Invalid 다음에 Valid를 출력할 수 있어서 발생하는 문제 같다.

