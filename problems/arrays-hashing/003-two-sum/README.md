# 3. Two Sum (Easy)

Given a list of integers `nums` and an integer `target`, return the indices `[i, j]` of two different elements whose values add up to `target`.

Exactly one valid pair exists. You may not use the same element twice. The two indices may be returned in either order.

## Examples

```
Input:  nums = [3, 4, 5, 6], target = 7
Output: [0, 1]      # 3 + 4 = 7

Input:  nums = [4, 5, 6], target = 10
Output: [0, 2]      # 4 + 6 = 10
```

## Constraints

- `2 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one solution exists.

## Hints

- A nested loop works but is O(n^2).
- For each number, what value would complete the pair? Can you look that up instantly?
