### Approach

A triplet can only help if none of its numbers is bigger than the matching number in the target, because merging takes the maximum of each position and could never come back down. Keep only those usable triplets, take the position-wise maximum over all of them, and check whether that equals the target.

### Complexity

- Time: O(n).
- Space: O(1).
