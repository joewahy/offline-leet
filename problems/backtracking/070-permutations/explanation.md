### Approach

Build each permutation by choosing which unused number goes next. The recursion keeps the path built so far and the numbers still unused. For each unused number, add it to the path and recurse on the rest without it. When no numbers are left, the path is a full permutation.

### Complexity

- Time: O(n * n!), there are n! permutations and each takes O(n) to build.
- Space: O(n) extra, not counting the output.

### Alternatives

Swapping elements in place and undoing the swap on the way back avoids creating new lists at each step.
