### Approach

Answer the queries in increasing order, so you can sweep the intervals once. For each query, add every interval that starts at or before it to a min-heap keyed by size (and also storing its end). Then discard intervals from the top that end before the query, since they can never help it or any later query. The top of the heap is then the smallest interval that contains the query, or there is none and the answer is -1.

The answers are stored by query value, so queries given in any order, with repeats, still come out in their original order.

### Complexity

- Time: O((n + q) log(n + q)) for the sorting and heap operations.
- Space: O(n + q).

### Alternatives

Checking every interval for every query is O(n * q), which times out on large inputs.
