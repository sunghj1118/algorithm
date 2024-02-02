# 입력값이 온점 하나가 들어오면 종료
while True:
    str = input()

    if str == '.':
        break

    # str에서 괄호만 추출
    stack = []
    balanced = True

    for i in str:
        if i in '([':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print('yes')
    else:
        print('no')
