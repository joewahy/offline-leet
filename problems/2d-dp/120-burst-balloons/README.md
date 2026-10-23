# 120. Burst Balloons (Hard)

There are `n` balloons, and balloon `i` has the number `nums[i]` painted on it. You burst every balloon, one at a time. When you burst balloon `i` you earn `left * nums[i] * right` coins, where `left` and `right` are the numbers on the balloons currently next to it. If a neighbour does not exist, treat it as a balloon with the number `1`.

Return the maximum number of coins you can collect by choosing the best order.

## Examples

```
Input:  nums = [3, 1, 5, 8]
Output: 167        # burst 1, 5, 3, 8

Input:  nums = [1, 5]
Output: 10
```

## Constraints

- `1 <= len(nums) <= 60`
- `0 <= nums[i] <= 100`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Choosing the first balloon to burst is hard, because the neighbours change. Try thinking about the last balloon to burst instead.
2. If balloon `k` is the last one burst in a range, its neighbours are the fixed borders of the range, and the two sides become independent subproblems.
3. Pad `nums` with `1` on both ends. `dp[l][r]` is the best for the balloons strictly between `l` and `r`: the maximum over `k` of `dp[l][k] + dp[k][r] + a[l] * a[k] * a[r]`. Fill it by increasing range length. This is O(n^3).

</details>
