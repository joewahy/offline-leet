# 36. Merge Two Sorted Lists (Easy)

You are given the heads of two linked lists that are each sorted in ascending order. Merge them into one sorted list by splicing together the existing nodes, and return the head of the merged list.

## Examples

```
Input:  list1 = [1, 2, 4], list2 = [1, 3, 5]
Output: [1, 1, 2, 3, 4, 5]

Input:  list1 = [], list2 = [0]
Output: [0]
```

## Constraints

- `0 <= length of each list <= 5000`
- `-1000 <= node.val <= 1000`

## Hints

- A dummy head node makes the first insertion the same as every other one.
