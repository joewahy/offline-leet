### Approach

The median splits all the numbers into a left half and a right half of nearly equal size. Instead of merging, binary search for how many elements of the shorter list belong in the left half. If `i` come from the shorter list, then `half - i` must come from the other one.

A split is right when the largest value on the left of each list is no bigger than the smallest value on the right of the other list. If the shorter list's left side is too big, move the split left. Otherwise move it right. With a correct split, the median is the larger of the two left maximums (odd total) or the average of that and the smaller of the right minimums (even total). Infinity values stand in for a split at the very edge of a list.

### Complexity

- Time: O(log(min(m, n))), searching only the shorter list.
- Space: O(1).

### Alternatives

Merging both lists and reading the middle is O(m + n), which is simpler but not logarithmic.
