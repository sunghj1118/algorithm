# DFS

This is yet another DFS problem so that I can become used to the algorithm. 

### While not 0 input
I need to take input such that the algorithm quits once the width and height aren't both 0. However, I also need to take a first input to start the program. So my program needs to take W, H once outside the while loop and once inside the while loop. How can I fix this such that it doesn't do so?

A recursion error arose so I decided to add a break statement if the width and height are 0.

This didn't work so the problem is likely the DFS function itself. I decided to change the structure into a iterative stack.
The iterative stack adds all possible directions into a local stack and pops them if they don't satisfy the conditions: x out of bounds, y out of bounds or map already visited.

Apparently this makes the function faster and handles recursion errors.