from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        stack = []

        # iterate through tokens
        for token in tokens:
            # if token is an operator
            if token in "+-*/":
                # pop two operands
                op2 = stack.pop()
                op1 = stack.pop()

                # perform operation
                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op1 - op2)
                elif token == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
            else:
                # push operand to stack
                stack.append(int(token))

        # return top of stack
        return stack.pop()
