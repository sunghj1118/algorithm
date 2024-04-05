# 19948. Problem Review

## 19948. 음유시인 영재

### Problem Definition
감수성이 뛰어난 음유시인 영재는 일상생활 중에 번뜩 시상이 떠오르곤 한다.

하지만 기억력이 좋지 못한 영재는 시상이 떠오르면 그 순간 컴퓨터로 기록해야만 안 까먹는다! 시는 대문자, 소문자 알파벳과 빈칸으로 이루어져 있다. 시상은 매번 훌륭하지만 제목 짓는 센스가 부족한 영재는 시에 나오는 단어들의 첫 글자를 대문자로 바꾼 뒤 순서대로 이어서 제목으로 만든다. 만약 시의 내용이 'There is no cow level' 이라면 시의 제목은 'TINCL'이 된다.

시도 때도 없이 시를 기록하느라 낡아버린 영재의 키보드는 수명이 얼마 남지 않았다. 앞으로 스페이스 바와 영자판을 누를 수 있는 횟수가 정해져 있어 이를 초과하면 키보드가 수명이 다 하여 어떠한 작업도 하지 못하게 된다. 하나 다행인 점은, 키보드를 쓸 때 같은 문자가 연속으로 나오거나 빈칸이 연속으로 나오는 경우 영재는 자판을 꾹 눌러 한 번만 사용해서 키보드를 좀 더 효율적으로 쓸 수 있다. (A와 a는 다른 문자이므로 'Aa'는 2번의 a자판을 누른 것으로 한다.)

시의 내용과 시의 제목은 Enter 키로 구분된다. 다행히 Shift 키와 Enter 키는 항상 수명이 무한한 상황이다!

음유시인 영재가 이번에 지은 시의 내용과 스페이스 바와 영자판을 누를 수 있는 횟수가 주어졌을 때, 시의 내용과 제목을 모두 기록할 수 있다면 시의 제목을 출력하고, 만약 키보드의 수명이 다 하여 기록을 완벽하게 못 하게 된다면 -1을 출력하여라. 

### Approach
- make an array of the poem
- get the durability of the space key
- get the remaining durability of each letter in the keyboard in a dictionary
- Calculate whether the poem can be typed with spaces
- skip if the letter is the same as the last letter
- last_letter = letter # update the last letter
- if the letter is uppercase, convert it to lowercase
- decrease the durability of the letter
- if the durability of the letter is less than 0, print -1 and break
- Print the first letter of each word in the poem

### Solution

```python
# Url: https://www.acmicpc.net/problem/19948

# make an array of the poem
poem = input().split()

# get the durability of the space key
n = int(input())

# get the remaining durability of each letter in the keyboard in a dictionary
durability = list(map(int, input().split()))

# Calculate whether the poem can be typed with spaces
if n < len(poem):
    print(-1)

last_letter = ''
for word in poem:
    for letter in word:
        # skip if the letter is the same as the last letter
        if letter == last_letter:
            continue
        last_letter = letter # update the last letter

        # if the letter is uppercase, convert it to lowercase
        if letter.isupper():
            letter = letter.lower()
        
        # decrease the durability of the letter
        durability[ord(letter) - ord('a')] -= 1

        # if the durability of the letter is less than 0, print -1 and break
        if durability[ord(letter) - ord('a')] < 0:
            print(-1)
            break

# Print the first letter of each word in the poem
for word in poem:
    print(word[0].upper(), end='')
```