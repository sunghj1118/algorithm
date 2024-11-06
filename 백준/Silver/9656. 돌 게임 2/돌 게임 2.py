def dp(n):
    li = [''] * (n+2)
    li[0] = 'CY'
    li[1] = 'SK'
    li[2] = 'CY'

    if n <= 3:
        return li[n-1]

    for i in range(3, n):
        li[i] = li[i-2]
    
    return li[n-1]

print(dp(int(input())))