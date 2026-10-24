### Approach

Track the farthest index you can reach so far. Walk the list: if the current index is beyond that reach, you are stuck and the end is unreachable. Otherwise update the reach with `i + nums[i]`. If you get through the whole list, the end is reachable.

### Complexity

- Time: O(n).
- Space: O(1).

### Alternatives

A DP that marks each index as reachable and checks every earlier index is O(n^2).
