# 38. Reorder List (Medium)

You are given the head of a singly linked list `L0 -> L1 -> ... -> Ln`. Rearrange it in place into

`L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`

Do not create new nodes or change node values; only change the `next` pointers. The function returns nothing; the list reachable from `head` afterwards is checked.

## Examples

```
Input:  head = [2, 4, 6, 8]
Output: [2, 8, 4, 6]

Input:  head = [2, 4, 6, 8, 10]
Output: [2, 10, 4, 8, 6]
```

## Constraints

- `1 <= number of nodes <= 5000`
- `1 <= node.val <= 1000`

## Hints

- Find the middle, reverse the second half, then weave the two halves together.
