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

## Hints

- You need a minimum spanning tree. Prim's algorithm on a complete graph is O(n^2); Kruskal with union-find also works.
