### Approach

If the total gas is less than the total cost, no start works, so return -1. Otherwise a start exists. Walk the stations while tracking the tank. When the tank goes negative at station `i`, no station from the current start up to `i` can be the answer, because each of them would have run dry by this point as well, so restart at `i + 1` with an empty tank. The final start is the answer.

### Complexity

- Time: O(n).
- Space: O(1).

### Alternatives

Trying every starting station and simulating the loop is O(n^2).
