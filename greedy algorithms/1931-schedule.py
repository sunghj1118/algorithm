N = int(input())
schedule = []
for meetings in range(0, N):
    schedule.append(list(map(int, input().split())))

schedule.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for i in range(N):
    #if the beginning of the next class starts after the end of current, add counter
    #the next class is now the current class (schedule[0][1])
    if end <= schedule[i][0]:
        count += 1
        end = schedule[i][1]

print(count)