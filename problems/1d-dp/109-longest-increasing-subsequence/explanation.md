### Approach

Keep a list `tails` where `tails[i]` is the smallest possible last value of an increasing subsequence of length `i + 1`. This list is always sorted. For each number, binary search for the first tail that is not smaller than it. If there is none, the number extends the longest subsequence, so append it. Otherwise it replaces that tail, which keeps a smaller ending value available for later.

The length of `tails` at the end is the answer. Note that `tails` is not itself the subsequence.

### Complexity

- Time: O(n log n).
- Space: O(n).

### Alternatives

The simple DP, where `dp[i]` is the best length ending at `i`, is O(n^2) time.
