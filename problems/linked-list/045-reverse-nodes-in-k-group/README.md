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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Handle one group at a time. First check whether `k` nodes are left.
2. For a full group, reverse just those `k` nodes, then reconnect the group to the part before it and the part after it.
3. Keep `group_prev` (the node before the group). Find the `k`-th node; if it does not exist, stop. Reverse the nodes up to `kth.next`, then set `group_prev.next = kth` and move `group_prev` to the old first node of the group. A dummy head helps.

</details>
