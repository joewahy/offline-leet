# 82. Clone Graph (Medium)

You are given a reference to one node of a connected, undirected graph. Return a deep copy (clone) of the whole graph: brand-new nodes with the same values and the same connections, none of them shared with the original.

Each `Node` has an integer `val` and a list `neighbors`. In the tests, a graph is written as an adjacency list: entry `i` lists the values of the neighbours of the node with value `i + 1`. Your function receives the node with value `1` (or `None` for an empty graph).

## Examples

```
Input:  adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
Output: a deep copy with the same adjacency list

Input:  adjList = [[]]
Output: a copy of a single node with no neighbours
```

## Constraints

- `0 <= number of nodes <= 1000`
- `1 <= Node.val <= 1000`, and every value is unique
- No repeated edges and no self-loops; the graph is connected.

## Hints

- Keep a dictionary from each original node to its clone, so you create each clone once and can reuse it when you meet the node again.
