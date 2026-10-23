# 44. Merge k Sorted Lists (Hard)

You are given a list `lists` of `k` linked lists, each sorted in ascending order. Merge them all into one sorted linked list and return its head.

## Examples

```
Input:  lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
Output: [1, 1, 2, 3, 3, 4, 5, 6]

Input:  lists = []
Output: []
```

## Constraints

- `0 <= k <= 100`
- `0 <= length of each list <= 100`, and the total number of nodes is at most `10000`
- `-1000 <= node.val <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Merging two sorted lists is easy. How could you reuse that idea for `k` lists?
2. Either merge pairs of lists repeatedly (like merge sort), or keep a min-heap holding the current head of each list.
3. With a heap, pop the smallest node, append it to the result, and push that node's `next`. Store `(value, list_index, node)` so ties never compare nodes. This is O(N log k) for N total nodes.

</details>
