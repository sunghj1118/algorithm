# take inputs K, N
K, N = list(map(int,input().split()))

# initialize list of cables
cables = []

# take inputs of cables
for i in K:
    cables.append(int(input()))

# set start as 1 and end as the longest cable available
start = 1
end = max(cables)

#while list until start is larger than end
#mid is the sum of start, end long divided by 2
#initialize numcables to 0 every loop
#for loop for every cable in the cable list
while(start<=end):
    mid = (start+end) // 2
    numcables = 0

    for i in cables:
        numcables = numcables + i//mid
    
    if(numcables >= N):
        start = mid +1
    else:
        end = mid-1


#if the number of cables that can be made is smaller than the needed N,
#update the start var to mid+1

#else, update end var to mid-1 to search for the largest end var possible
#aka longest cable possible

print(end)