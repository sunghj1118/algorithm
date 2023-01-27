# take inputs N, M
Ntrees, Mneeded = list(map(int,input().split()))

# initialize list of trees
# take inputs of trees
trees = list(map(int,input().split()))


# set start as 1 and end as the longest tree available
start = 1
end = max(trees)

#while list until start is larger than end
#mid is the sum of start, end long divided by 2
#initialize treelen to 0 every loop
#for loop for every tree in the tree list
while(start <= end):
    mid = (start+end) // 2
    treelen = 0

    for i in trees:
        if(i > mid):
            treelen += i - mid
    
    if(treelen >= Mneeded):
        start = mid +1
    else:
        end = mid-1


#if the number of trees that can be made is smaller than the needed N,
#update the start var to mid+1

#else, update end var to mid-1 to search for the largest end var possible
#aka longest tree possible

print(end)