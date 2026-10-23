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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The new order alternates between the front of the list and the back. You cannot walk backwards in a singly linked list, so what can you prepare?
2. Split the list at its middle, reverse the second half, then weave the two halves together one node at a time.
3. Find the middle with slow and fast pointers, cut the list there (`slow.next = None`), reverse the second part, then repeatedly link `first -> second -> first's old next -> ...`. This needs O(1) extra space.

</details>
