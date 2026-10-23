# 45. Reverse Nodes in k-Group (Hard)

Given the head of a linked list and an integer `k`, reverse the nodes of the list `k` at a time and return the new head.

If the number of remaining nodes at the end is less than `k`, leave those nodes as they are. You may only change node pointers, not node values.

## Examples

```
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]

Input:  head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

## Constraints

- `1 <= k <= number of nodes <= 5000`
- `0 <= node.val <= 1000`

## Hints

- Check that `k` nodes remain before reversing a group, then reconnect the reversed group to the rest.
