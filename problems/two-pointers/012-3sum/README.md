# 12. 3Sum (Medium)

Given a list of integers `nums`, return every distinct triplet `[a, b, c]` of values taken from three different positions such that `a + b + c == 0`.

The same combination of values must not appear twice in the answer. The triplets and the numbers inside them may be returned in any order.

## Examples

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:  nums = [0, 1, 1]
Output: []
```

## Constraints

- `3 <= len(nums) <= 3000`
- `-10^5 <= nums[i] <= 10^5`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Reduce it to a problem you know: if you fix one number, what remains is a two-sum for the negative of it.
2. Sort the array, fix each number `a` in turn, and use two pointers on the part to its right to find pairs summing to `-a`.
3. To avoid duplicate triplets, skip a value equal to the previous one for `a`, and after finding a triplet move the left pointer past equal values. Stop early when `a > 0`.

</details>
