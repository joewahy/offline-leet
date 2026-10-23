# 40. Copy List with Random Pointer (Medium)

Each node of a linked list has a `val`, a `next` pointer, and a `random` pointer that may point to any node in the list or be `None`.

Build a deep copy of the list: create brand-new nodes with the same values, where every `next` and `random` pointer in the copy points to nodes of the copy (never to the original). Return the head of the copy.

In the tests a list is written as `[[val, random_index], ...]`, where `random_index` is the position of the node `random` points to, or `null`.

## Examples

```
Input:  [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
Output: a deep copy with the same structure

Input:  [[1, 1], [2, 1]]
Output: a deep copy with the same structure
```

## Constraints

- `0 <= number of nodes <= 1000`
- `-100 <= node.val <= 100`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The hard part is the `random` pointer: it may point to a node you have not copied yet.
2. Make all the copies first, remembering which original maps to which copy. Then wire up `next` and `random` using that mapping.
3. Use a dictionary `copies[original] = new node` (with `None` mapping to `None`). The first pass creates the nodes; the second pass sets `copy.next = copies[orig.next]` and `copy.random = copies[orig.random]`.

</details>
