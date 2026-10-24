### Approach

Treat the array as a linked list where index `i` points to `nums[i]`. Because there are `n + 1` values in the range `1..n`, two indices point to the same place, which means the list has a cycle, and the duplicate is where the cycle starts.

Use Floyd's algorithm. A slow and a fast pointer will meet inside the cycle. Then start a second slow pointer from the beginning. Moving both one step at a time, they meet at the entrance to the cycle, which is the duplicate value.

### Complexity

- Time: O(n).
- Space: O(1), and the array is not modified.

### Alternatives

A set of seen numbers is O(n) space. Sorting the array is O(n log n) time and changes the input.
