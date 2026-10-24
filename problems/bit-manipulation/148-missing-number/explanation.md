### Approach

The numbers `0..n` with one missing, plus the indices `0..n-1`, can be combined with XOR. Start with `n`, then XOR in every index and every value. Each number that is present appears twice (once as an index or the start, once as a value) and cancels. The missing number appears only once, so it is what is left.

### Complexity

- Time: O(n).
- Space: O(1).

### Alternatives

The sum formula `n * (n + 1) / 2 - sum(nums)` is just as fast. In languages with fixed-size integers it can overflow, which XOR cannot.
