# 150. Problem Review

## 150. Evaluate Reverse Polish Notation

### Problem Definition
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

### Approach
- Implement with stack.

### Solution

```python
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
