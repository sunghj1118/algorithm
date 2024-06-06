from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if hand is in multiples of groupSize
        if (len(hand) % groupSize) != 0:
            return False
        
        # count frequencies
        count = Counter(hand)

        # use a min-heap to process cards in ascending order
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0] # get the smallest value
            for i in range(groupSize): # check consecutive values and decrease if exists
                if count[first+i] == 0:
                    return False
                count[first + i] -= 1
                if count[first + i] == 0: # check if count has reached 0
                    if first + i != min_heap[0]: # if 0, need to check if it's the smallest val
                        return False # if it isn't, there's an inconsistency hence false
                    heapq.heappop(min_heap) # if smallest and 0, remove from heap
            
        # heap has been emptied
        return True