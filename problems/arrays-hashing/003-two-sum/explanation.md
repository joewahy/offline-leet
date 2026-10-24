### Approach

For each number `n`, the partner you need is `target - n`. Walk the list once, keeping a dictionary of the values already seen and where they were. If the partner is already in the dictionary, you have the pair. Otherwise record `n` and move on.

Looking up the partner before storing the current number also means an element is never paired with itself.

### Complexity

- Time: O(n), one pass with O(1) dictionary lookups.
- Space: O(n) for the dictionary.

### Alternatives

Checking every pair is O(n^2) time and O(1) space, and it times out on large inputs.
