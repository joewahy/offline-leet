# 1. Contains Duplicate (Easy)

Given a list of integers `nums`, return `True` if any value appears at least twice, and `False` if every value is distinct.

## Examples

```
Input:  nums = [1, 2, 3, 1]
Output: True

Input:  nums = [1, 2, 3, 4]
Output: False
```

## Constraints

- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

- Can you remember what you have already seen while scanning once?
- Aim for O(n) time.
