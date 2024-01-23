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
