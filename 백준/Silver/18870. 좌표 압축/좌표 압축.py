n = int(input())
li = list(map(int, input().split()))

set_li = sorted(set(li))

index_map = {val: idx for idx,val in enumerate(set_li)}

out = [index_map[x] for x in li]

print(' '.join(map(str, out)))