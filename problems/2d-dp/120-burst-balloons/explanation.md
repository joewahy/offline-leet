### Approach

Think about which balloon is burst last in a range, not first. If balloon `k` is the last one left between `lo` and `hi`, its neighbours at that moment are exactly `lo` and `hi`, so it earns `a[lo] * a[k] * a[hi]`. The ranges to the left and right of `k` are then independent subproblems.

So `dp[lo][hi]` is the best over all `k` in between of `dp[lo][k] + dp[k][hi] + a[lo] * a[k] * a[hi]`. Pad the array with a 1 on each end, and fill in by increasing range length.

### Complexity

- Time: O(n^3).
- Space: O(n^2).

### Watch out

Choosing which balloon to burst first does not split the problem, because the neighbours change afterwards. That is why the last balloon is the right choice.
