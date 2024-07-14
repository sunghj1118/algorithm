import statistics as st

n = int(input())
li = []

for i in range(n):
	li.append(int(input()))

print(round(sum(li)/n))
print(st.median(li))
if len(st.multimode(li)) > 1:
	print(sorted(st.multimode(li))[1])
else:
	print(st.mode(li))
print(max(li)-min(li))