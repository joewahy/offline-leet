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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A graph can have cycles, so you may reach the same node again. How do you avoid cloning it twice?
2. Keep a dictionary from each original node to its clone.
3. Traverse with DFS or BFS. When you first see a node, create its clone and store it. For each neighbour, make sure it has a clone, and append that clone to the current clone's `neighbors`.

</details>
