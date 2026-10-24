### Approach

Backtracking. Build a combination by choosing a number, subtracting it from the remaining target, and recursing. The same number can be reused, so the recursion restarts from the same index. To avoid the same combination in a different order, only ever choose numbers at or after the current index. A branch is dropped when the number is bigger than what remains.

### Complexity

- Time: exponential. It is bounded by the number of combinations explored, which depends on the target and the smallest candidate.
- Space: O(target / smallest number), the deepest path.

### Watch out

Copy the path (`path[:]`) when you record a result. Otherwise every saved answer shares one list that keeps changing.
