N = int(input())
schedule = []
for meetings in range(0, N):
    schedule.append(list(map(int, input().split())))

schedule.sort(key=lambda x: (x[1], x[0]))

count = 0

def scheduler(schedule):
    end = 0
    new_schedule = []
    for i in range(len(schedule)):
        #if the beginning of the next class starts after the end of current, add counter
        #the next class is now the current class (schedule[0][1])
        if end <= schedule[i][0]:
            end = schedule[i][1]
        else:
            new_schedule.append(schedule[i])
    schedule = new_schedule
    return schedule

while len(schedule) != 0:
    schedule = scheduler(schedule)
    count += 1

print(count)