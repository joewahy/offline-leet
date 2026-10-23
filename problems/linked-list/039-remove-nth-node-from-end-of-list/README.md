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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Counting from the end seems to need the length. Can you avoid a first pass over the whole list?
2. Use two pointers: move the lead pointer `n` steps ahead, then move both until the lead reaches the end.
3. Start both at a dummy node placed before the head. When the lead is at the last node, the trailing pointer is just before the node to remove, so set `trail.next = trail.next.next`. The dummy handles removing the head.

</details>
