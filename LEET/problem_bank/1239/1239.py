from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_length = 0

        def dfs(idx, cur):
            if len(set(cur)) != len(cur):
                return
            self.max_length = max(self.max_length, len(cur))
            for i in range(idx, len(arr)):
                dfs(i + 1, cur + arr[i])

        dfs(0, "")
        return self.max_length


print(Solution().maxLength(["un", "iq", "ue"]))
