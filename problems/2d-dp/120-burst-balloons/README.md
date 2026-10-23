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

## Hints

- Think of the last balloon to burst inside a range. Its neighbours are then fixed (the range's borders), which splits the problem into two independent smaller ranges.
