### Approach

A set keeps each value once, so if turning `nums` into a set makes it shorter, some value appeared twice. Comparing the two lengths answers the question in one line.

### Complexity

- Time: O(n). Building the set touches each element once, and each insert is O(1) on average.
- Space: O(n) for the set when every value is distinct.

### Alternatives

- Sorting first and comparing neighbours uses O(1) extra space but costs O(n log n) time.
- Checking every pair is O(n^2) and times out on large inputs.
