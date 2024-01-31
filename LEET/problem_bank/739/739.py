from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last_day = stack.pop()
                answer[last_day] = i - last_day
            stack.append(i)
        return answer


temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
print(Solution().dailyTemperatures(temperatures))
