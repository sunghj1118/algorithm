class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if (c=='(') or (c=='[') or (c=='{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                open_char = stack.pop()
                if (c==")" and open_char!="(") or (c=="]" and open_char!="[") or (c=="}" and open_char!="{"):
                    return False
        
        return stack == []