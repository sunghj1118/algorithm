# 11725: Rootless Tree

There is a rootless tree given. Assuming that the tree's root is 1, make a program to find each node's parent.

**Input**: <br>
line 1: amount of nodes <br>
lines 2~(N-1): connected nodes A and B

**Output**: <br>
lines 1~(N-1): parent nodes of nodes starting from node 2


# Planing
1. Initialize: First we need to take input.
To do this, I am going to use an adjacency list to implement the tree. The tree will store the children of the nodes and it is initialized as N+1 because the nodes start at 1.

2. DFS Function: We need our function to return the immediate parent of each node starting from node 2. However, I noticed that the first value of each node's children is the parent and decided that maybe this might be the answer without needing to implement DFS. However, of course, it never is that easy. <br>
<br> 
The next attempt was through DFS. If node 1 is called, the parent node would be 0, since there is no parent node. Somehow if I set a recursive function to call the next child while keeping track of the parent of each node, this might work.

3. Print results: After saving the parents into an array, we print all the values from node 2 onwards.

# Errors
**RecursionError (RuntimeError)**: After running at 1%, the problem faced a runtime error. This is probably due to Python's recursion low recursion limit.

The recursion error was still not solved after I set the recursion limit higher. This solved the problem, but it was still incredibly slow.
```python
import sys
sys.setrecursionlimit(10**6)
```

Due to limitations in speed, I decided to change the implementation to a stack based DFS since that would make the program faster. The stack based implementation also worked for the examples provided.