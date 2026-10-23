# 39. Remove Nth Node From End of List (Medium)

Given the head of a linked list and an integer `n`, remove the `n`-th node counted from the end of the list and return the head of the resulting list.

## Examples

```
Input:  head = [1, 2, 3, 4], n = 2
Output: [1, 2, 4]

Input:  head = [5], n = 1
Output: []
```

## Constraints

- `1 <= number of nodes <= 5000`
- `1 <= n <= number of nodes`
- `1 <= node.val <= 100`

## Hints

- Do it in one pass: move a lead pointer `n` steps ahead, then advance both pointers together.
