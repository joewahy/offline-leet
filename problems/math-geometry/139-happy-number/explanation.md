### Approach

Repeatedly replace the number by the sum of the squares of its digits. If it reaches 1, the number is happy. Otherwise the sequence falls into a loop and never gets there. So this is cycle detection: run a slow and a fast pointer over the sequence. If the fast one reaches 1 the number is happy, and if the two meet at a value other than 1, there is a loop.

### Complexity

- Time: O(log n) for the digits, since the sequence quickly drops to a small range and then cycles for a bounded number of steps.
- Space: O(1).

### Alternatives

Storing seen values in a set also works, with O(1) extra space replaced by a small set.
