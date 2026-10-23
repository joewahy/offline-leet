# 37. Linked List Cycle (Easy)

Given the head of a linked list, return `True` if the list contains a cycle (some node can be reached again by following `next` pointers), otherwise `False`.

In the tests, a list is described as `[values, pos]`: `pos` is the index of the node the last node points back to, or `-1` for no cycle. `pos` is not passed to your function.

## Examples

```
Input:  values = [1, 2, 3, 4], pos = 1     (4 points back to 2)
Output: True

Input:  values = [1, 2], pos = -1
Output: False
```

## Constraints

- `0 <= number of nodes <= 5000`
- `-10^5 <= node.val <= 10^5`

## Hints

- A set of visited nodes works. Can you do it with O(1) memory using a slow and a fast pointer?
