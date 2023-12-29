class Solution(object):
    def minCost(self, colors, neededTime):
        cost = 0
        i = 0

        while i < len(colors) - 1:
            if colors[i] == colors[i+1]:
                total_time = neededTime[i]
                max_time = neededTime[i]

                # Move through sequence of identical chars
                while i < len(colors)-1 and colors[i] == colors[i+1]:
                    total_time += neededTime[i+1]
                    max_time = max(max_time, neededTime[i+1])
                    i += 1

                cost += total_time - max_time
            else:
                i += 1

        return cost
