def dp(n):
    li = [''] * (n+2)
    li[0] = 'SK'
    li[1] = 'CY'
    li[2] = 'SK'

    if n <= 3:
        return li[n-1]

    for i in range(3, n):
        li[i] = li[i-2]
    
    return li[n-1]

print(dp(int(input())))