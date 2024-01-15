# 2225. Problem Review

## 2225. Find Players With Zero or One Losses

### Problem Definition
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

### Approach
- We have two tasks.
- We can solve them one by one.


### Solution
- Create dictionaries with frequency counts for each.
- 1. If players out of the winners are not in the losers dict, they have never lost.
- 2. If freq values for losers is 1, they have lost once.

```python
from typing import List
from collections import Counter


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Get lists of all winners and losers
        all_winners = []
        all_losers = []

        for n in matches:
            winner = n[0]
            loser = n[1]

            all_winners.append(winner)
            all_losers.append(loser)

        # Get frequencies of all winners and losers
        W_counters = Counter(all_winners)
        L_counters = Counter(all_losers)

        # For players in winners list, if they are not in the losers list, add them to the lost0 list
        lost0 = []
        for player in W_counters:
            if player not in L_counters:
                lost0.append(player)

        # For players that have have lost once, add them to the lost1 list
        lost1 = []
        for player in L_counters:
            if L_counters[player] == 1:
                lost1.append(player)

        lost0.sort()
        lost1.sort()
        return [lost0, lost1]
