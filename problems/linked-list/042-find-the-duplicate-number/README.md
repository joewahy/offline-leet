# 42. Find the Duplicate Number (Medium)

`nums` contains `n + 1` integers, each in the range `[1, n]`. Exactly one value is repeated (it may appear more than twice); every other value appears once.

Return the repeated value. You must not modify `nums`, and you should use only O(1) extra space.

## Examples

```
Input:  nums = [1, 2, 3, 2, 2]
Output: 2

Input:  nums = [1, 2, 3, 4, 4]
Output: 4
```

## Constraints

- `1 <= n <= 10000`
- `len(nums) == n + 1`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The values are between 1 and `n` and the array has `n + 1` entries. Treat each value as a pointer to another index.
2. Following `i -> nums[i]` must eventually repeat, so it forms a cycle, and the duplicate value is where the cycle begins.
3. Use Floyd's algorithm: find where a slow and a fast pointer meet, then restart one pointer from index 0 and move both one step at a time. They meet at the cycle entrance, which is the duplicate.

</details>
