# 41. Add Two Numbers (Medium)

Two non-negative integers are stored in two linked lists, one digit per node, with the least significant digit first. For example `342` is stored as `[2, 4, 3]`.

Add the two numbers and return the sum as a linked list in the same format.

## Examples

```
Input:  l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]          # 342 + 465 = 807

Input:  l1 = [9, 9], l2 = [1]
Output: [0, 0, 1]          # 99 + 1 = 100
```

## Constraints

- `1 <= number of nodes in each list <= 3000`
- `0 <= node.val <= 9`
- No list has leading zeros, except the number `0` itself.

## Hints

- Add digit by digit and carry the overflow, like on paper. Don't forget a final carry.
