# take inputs N, M, L
current_stops, stops_to_build, length = list(map(int,input().split()))

# take inputs of stops and sort
stops = list(map(int,input().split()))
stops.sort()

# make list with distances between stops
distances = []
distances.append(stops[0])
for i in range(len(stops)-1):
    distances.append(stops[i+1] - stops[i])
distances.append(length - stops[-1])
print(distances)

# set start as 1 and end as the longest dist available
start = 1
end = max(distances)

#while list until start is larger than end
#mid is the sum of start, end long divided by 2
#initialize distlen to 0 every loop
#for loop for every dist in the dist list
while(start <= end):
    mid = (start+end) // 2
    nstops = 0
    newdist =[]

    for i in distances:
        divisible = i // mid
        
        if(i//mid > 0):
            nstops += divisible
            divisible += 1
            for j in range(divisible):
                newdist.append(i//divisible)
            if(i%divisible != 0):
                newdist[-1] += (i%divisible)
        else:
            newdist.append(i)
    
    if(nstops == stops_to_build):
        start = end+1
    if(nstops > stops_to_build):
        start = mid +1
    else:
        end = mid-1


#if the number of stops that can be made is smaller than the needed N,
#update the start var to mid+1

#else, update end var to mid-1 to search for the largest end var possible
#aka longest dist possible

print(max(newdist))