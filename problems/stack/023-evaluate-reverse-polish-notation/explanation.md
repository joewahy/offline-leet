### Approach

In reverse Polish notation an operator applies to the two most recent values. Push numbers on a stack. On an operator, pop the right operand first, then the left one, apply the operator, and push the result. The single value left at the end is the answer.

### Complexity

- Time: O(n).
- Space: O(n), when many numbers come before the operators.

### Watch out

Division must truncate toward zero, but Python's `//` rounds down. The reference divides the absolute values and fixes the sign afterwards, so `-7 / 2` gives `-3`, not `-4`.
