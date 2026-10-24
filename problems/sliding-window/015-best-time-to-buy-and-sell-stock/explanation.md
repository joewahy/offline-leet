### Approach

Walk the prices once and keep the lowest price seen so far. Selling today would earn `price - lowest`, so track the best of those values. You never need to know which day you bought on, only the profit.

### Complexity

- Time: O(n).
- Space: O(1).

### Alternatives

Trying every buy and sell pair is O(n^2) and times out on large inputs.
