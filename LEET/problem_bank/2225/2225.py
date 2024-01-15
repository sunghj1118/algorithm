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


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
           [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
solution = Solution()
print(solution.findWinners(matches))
