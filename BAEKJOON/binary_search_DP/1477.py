# take inputs N, M, L
current_stops, stops_to_build, length = list(map(int,input().split()))

# take inputs of stops and sort
stops = [0] + list(map(int,input().split())) + [length]
stops.sort()

# make list with distances between stops
distances = [stops[i+1] - stops[i] for i in range(len(stops)-1)]

# set start as 1 and end as the longest dist available
start, end = 1, length
result = 0

#while list until start is larger than end
#mid is the sum of start, end long divided by 2
#initialize nstops to 0 every loop
while(start <= end):
    mid = start + (end - start) // 2
    nstops = 0

    for i in distances:
        if (i > mid):
            nstops += (i - 1) // mid
    
    if(nstops <= stops_to_build):
        result = mid
        end = mid-1
    else:
        start = mid+1


#if the number of stops that can be made is smaller than the needed N,
#update the start var to mid+1

#else, update end var to mid-1 to search for the largest end var possible
#aka longest dist possible

print(result)