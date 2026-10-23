# 35. Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list and return the new head.

## Examples

```
Input:  head = [0, 1, 2, 3]
Output: [3, 2, 1, 0]

Input:  head = []
Output: []
```

## Constraints

- `0 <= number of nodes <= 5000`
- `-5000 <= node.val <= 5000`

## Hints

- Walk the list once, pointing each node back at the node before it.
- You can also do it recursively.
