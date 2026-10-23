# 94. Min Cost to Connect All Points (Medium)

`points[i] = [x, y]` is a point on a 2D plane. You may connect two points by a wire whose cost is their Manhattan distance, `|x1 - x2| + |y1 - y2|`.

Return the minimum total cost needed so that every point is connected to every other point through some chain of wires (exactly one simple path between any two points).

## Examples

```
Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Input:  points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- `1 <= len(points) <= 1000`
- `-10^6 <= x, y <= 10^6`, and all points are distinct

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You need to connect all the points with the smallest total wire length. This is a minimum spanning tree.
2. Use Prim's or Kruskal's algorithm on the complete graph where each edge's weight is the Manhattan distance.
3. Prim's: keep the best known distance from the tree to each outside point. Repeatedly add the closest outside point and update the others. That is O(n^2), which suits a complete graph.

</details>
