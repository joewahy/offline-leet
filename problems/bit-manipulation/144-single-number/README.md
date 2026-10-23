# 144. Single Number (Easy)

In the list `nums`, every integer appears exactly twice except for one integer that appears once. Return the integer that appears once.

Use O(n) time and O(1) extra space.

## Examples

```
Input:  nums = [3, 2, 3]
Output: 2

Input:  nums = [7, 6, 6, 7, 8]
Output: 8
```

## Constraints

- `1 <= len(nums) <= 9999` (always odd)
- `-30000 <= nums[i] <= 30000`

## Hints

- XOR of a number with itself is `0`, and XOR with `0` leaves a number unchanged. XOR everything together.
