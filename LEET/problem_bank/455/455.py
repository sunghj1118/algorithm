class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        max_cookies = 0
        cookie_index = 0
        g.sort()
        s.sort()
        for greed in g:
            while cookie_index < len(s):
                if s[cookie_index] >= greed:
                    max_cookies += 1
                    cookie_index += 1
                    break  # Current child is satisfied, move on to next child
                cookie_index += 1  # Current cookie is too small, move on to next cookie

        return max_cookies
