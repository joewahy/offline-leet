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

## Hints

- A min-heap holding the current head of every list gives the next smallest node in O(log k).
- Alternatively, merge the lists pairwise, like merge sort.
