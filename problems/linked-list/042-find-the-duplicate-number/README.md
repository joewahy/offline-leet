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

## Hints

- Treat `nums[i]` as a "next" pointer from index `i`. The duplicate is where two paths enter the same cycle.
- Floyd's tortoise and hare finds the cycle entrance.
