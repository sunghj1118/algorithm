from collections import defaultdict

def channel_changes(N, M, P, preferences):
    # Create a dictionary to store who hates each channel
    haters = defaultdict(list)
    for i, (fav, hate) in enumerate(preferences):
        haters[hate].append(i)
    
    changes = 0
    visited = set()
    current = P

    while True:
        if current in visited:
            return -1  # We've entered a loop
        
        visited.add(current)
        
        if current not in haters:
            return changes  # No one hates this channel, we're done
        
        # Find the youngest person who hates this channel
        youngest = min(haters[current])
        
        # Change to their favorite channel
        current = preferences[youngest][0]
        changes += 1

# Read input
N, M, P = map(int, input().split())
preferences = [tuple(map(int, input().split())) for _ in range(N)]

result = channel_changes(N, M, P, preferences)
print(result)