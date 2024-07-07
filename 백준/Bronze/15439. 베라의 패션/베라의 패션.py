# 15439
# possible different color combinations for each shirt
# is equal to n-1.
# when n = 1, possible combinations are n(n-1)=0
# when n = 2, 2(2-1) = 2
# when n = 5, 5(5-1) = 20

n = int(input())
print(n*(n-1))