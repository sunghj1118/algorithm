# 455. Problem Review

## 455. Assign Cookies

### Problem Definition
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

- Have a list of of cookies and list of children's greed.

### Approach
- Order the children's greed and cookies in ascending order.
- If there exists a cookie larger than the greed factor of the child, cycle through the cookies to provide the smallest cookie larger than the greed.

### Attempt 1
```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        max_cookies = 0
        g.sort()
        s.sort()
        for greed in g[:]:
            for cookie in s[:]:
                if cookie < greed:
                    max_cookies += 1
                    s.remove(cookie)
                else:
                    break

        return max_cookies
```

### Solution
Provide a detailed explanation of your solution. Include code snippets if possible.

```python
# Code snippet here
