class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        total_score = 0
        if x >= y:
            s, score = remove_pairs(s, 'a', 'b', x)
            total_score += score
            s, score = remove_pairs(s, 'b', 'a', y)
        else:
            s, score = remove_pairs(s, 'b', 'a', y)
            total_score += score
            s, score = remove_pairs(s, 'a', 'b', x)

        total_score += score
        return total_score