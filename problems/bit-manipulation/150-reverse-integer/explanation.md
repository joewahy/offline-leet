### Approach

Peel digits off the end and push them onto a new number: take `x % 10`, and append it with `rev * 10 + digit`. Handle the sign separately, by reversing the absolute value and applying the sign at the end. If the result does not fit in a signed 32-bit integer, return 0.

### Complexity

- Time: O(log x), one step per digit.
- Space: O(1).

### Watch out

Python integers cannot overflow, so the 32-bit range check at the end is what enforces the problem's rule.
