# 4852: Winter Festival

Sequences of parties that consist of several pairs of guests will be given. For example, if the string 'Marie Sally' is given, then Marie gave a present to Sally. The end of a party is marked by a '#' character, and another '#' marks the end of the sequence of parties.

I need to find out the closed cycles within each party.

## Steps
1. Take input as input string.
    - Parse string into parties.
    - For each party, create a directed graph where nodes represent guests and edges represent the act of giving a present.
2. DFS Function:
    - Define a DFS function to explore the graph from a given node.
    - This function should also keep track of the path taken and check for cycles.
3. Detecting Cycles:
    - For each node (guest) in the party, call the DFS function.
    - During DFS, if you encounter a node that is already in the current path, a cycle is detected. Record this cycle.
4. Handling Visited Nodes:
    - Mark nodes as visited as you traverse them to avoid redundant checks.
    - However, ensure that you only mark a node as visited in the current DFS call to detect cycles effectively.
5. Output Closed Cycles:
    - After completing DFS for a party, output all detected cycles.
    - Repeat the process for each party.
6. End of Input:
    - Stop processing when you encounter the second '#' character marking the end of all parties.