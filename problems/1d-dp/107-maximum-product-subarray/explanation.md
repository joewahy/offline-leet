### Approach

A negative number can turn the smallest product into the largest, so track both the biggest and the smallest product of a subarray ending at the current position. For each number, the new maximum and minimum come from the number itself, or the number times the previous maximum or minimum. The best answer so far is the largest maximum seen.

### Complexity

- Time: O(n).
- Space: O(1).

### Watch out

Compute both new values from the old ones before assigning either, or the second uses an already updated number. The tuple assignment does this.
