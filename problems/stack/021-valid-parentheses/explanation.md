### Approach

Every closing bracket must match the most recent unclosed opening bracket, which is exactly what a stack gives you. Push opening brackets. On a closing bracket, pop and check it is the matching opener. At the end the stack must be empty, or some bracket was never closed.

### Complexity

- Time: O(n), one pass.
- Space: O(n), when the input is all opening brackets.

### Watch out

Check for an empty stack before popping, so a string that starts with a closing bracket returns `False` instead of raising an error.
