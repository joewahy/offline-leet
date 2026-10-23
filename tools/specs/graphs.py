from spec import P

CATEGORY = "graphs"

INF = 2147483647


def _grid(rng, rows, cols, p, one="1", zero="0"):
    return [[one if rng.random() < p else zero for _ in range(cols)] for _ in range(rows)]


def _igrid(rng, rows, cols, p):
    return [[1 if rng.random() < p else 0 for _ in range(cols)] for _ in range(rows)]


def _islands_gen(rng):
    out = [[_grid(rng, r, c, p)] for r, c, p in ((1, 5, 0.5), (3, 3, 0.5), (4, 6, 0.4), (6, 6, 0.6))]
    out += [[_grid(rng, 60, 60, 0.45)], [_grid(rng, 60, 60, 1.0)], [_grid(rng, 60, 60, 0.2)]]
    return out


def _area_gen(rng):
    out = [[_igrid(rng, r, c, p)] for r, c, p in ((1, 5, 0.5), (3, 3, 0.5), (4, 6, 0.4), (6, 6, 0.6))]
    out += [[_igrid(rng, 60, 60, 0.55)], [_igrid(rng, 60, 60, 1.0)]]
    return out


def _connected(rng, n, extra):
    adj = {i: set() for i in range(1, n + 1)}
    for v in range(2, n + 1):
        u = rng.randint(1, v - 1)
        adj[u].add(v)
        adj[v].add(u)
    for _ in range(extra):
        a, b = rng.randint(1, n), rng.randint(1, n)
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    return [sorted(adj[i]) for i in range(1, n + 1)]


def _clone_gen(rng):
    return [[_connected(rng, n, rng.randint(0, n))] for n in (1, 2, 4, 8, 20)] + [[_connected(rng, 1000, 1500)], [[]]]


def _rooms(rng, rows, cols):
    return [[rng.choice([-1, 0, INF, INF, INF]) for _ in range(cols)] for _ in range(rows)]


def _rooms_gen(rng):
    return [[_rooms(rng, r, c)] for r, c in ((1, 3), (3, 3), (4, 5), (6, 6))] + [[_rooms(rng, 60, 60)]]


def _oranges(rng, rows, cols):
    return [[rng.choice([0, 1, 1, 1, 2]) for _ in range(cols)] for _ in range(rows)]


def _oranges_gen(rng):
    out = [[_oranges(rng, r, c)] for r, c in ((1, 4), (3, 3), (4, 5), (5, 5))]
    snake = [[1] * 60 for _ in range(60)]
    snake[0][0] = 2
    out += [[_oranges(rng, 60, 60)], [snake]]
    return out


def _heights(rng, rows, cols, hi=6):
    return [[rng.randint(0, hi) for _ in range(cols)] for _ in range(rows)]


def _pacific_gen(rng):
    return [[_heights(rng, r, c)] for r, c in ((1, 1), (1, 5), (4, 1), (3, 3), (5, 5), (6, 8))] + [[_heights(rng, 30, 30, 20)]]


def _xo(rng, rows, cols, p=0.55):
    return [["O" if rng.random() < p else "X" for _ in range(cols)] for _ in range(rows)]


def _xo_gen(rng):
    return [[_xo(rng, r, c)] for r, c in ((1, 3), (3, 3), (4, 5), (6, 6), (8, 8))] + [[_xo(rng, 60, 60, 0.6)], [_xo(rng, 60, 60, 0.9)]]


def _courses(rng, n, m, acyclic):
    order = list(range(n))
    rng.shuffle(order)
    pos = {c: i for i, c in enumerate(order)}
    edges = set()
    for _ in range(m):
        a, b = rng.sample(range(n), 2) if n > 1 else (0, 0)
        if n > 1:
            if acyclic and pos[a] < pos[b]:
                a, b = b, a
            edges.add((a, b))
    return [n, [list(e) for e in sorted(edges)]]


def _courses_gen(rng):
    out = [_courses(rng, n, m, a) for n, m, a in ((3, 3, True), (5, 6, True), (5, 8, False), (8, 10, True), (8, 12, False))]
    out.append([1, []])
    out.append(_courses(rng, 2000, 3000, True))
    chain = [[i + 1, i] for i in range(1999)]
    out.append([2000, chain])
    out.append([2000, chain + [[0, 1999]]])
    return out


def _courses_small(rng):
    n = rng.randint(1, 6)
    return _courses(rng, n, rng.randint(0, 7), rng.random() < 0.6)


def _tree_edges(rng, n):
    edges = [[rng.randint(0, v - 1), v] for v in range(1, n)]
    return [e if rng.random() < 0.5 else e[::-1] for e in edges]


def _valid_tree_gen(rng):
    out = []
    for n in (2, 5, 9, 20):
        e = _tree_edges(rng, n)
        out.append([n, e])
        bad = [list(x) for x in e]
        bad[rng.randrange(len(bad))] = rng.sample(range(n), 2)
        out.append([n, bad])
        out.append([n, e[:-1]])
    out.append([3000, [[i, i + 1] for i in range(2999)]])
    out.append([3000, [[i, i + 1] for i in range(2999)] + [[0, 2999]]])
    return out


def _tree_small(rng):
    n = rng.randint(1, 7)
    e = _tree_edges(rng, n)
    r = rng.random()
    if r < 0.3 and e:
        e.pop()
    elif r < 0.6 and n > 1:
        e.append(rng.sample(range(n), 2))
    return [n, e]


def _components_gen(rng):
    out = []
    for n, m in ((1, 0), (4, 2), (8, 5), (12, 9)):
        out.append([n, _rand_edges(rng, n, m)])
    out.append([5000, _rand_edges(rng, 5000, 3500)])
    out.append([5000, _rand_edges(rng, 5000, 900)])
    return out


def _rand_edges(rng, n, m):
    seen = set()
    while len(seen) < m and len(seen) < n * (n - 1) // 2:
        a, b = sorted(rng.sample(range(n), 2))
        seen.add((a, b))
    return [list(e) for e in sorted(seen)]


def _redundant(rng, n):
    edges = [[rng.randint(1, v - 1), v] for v in range(2, n + 1)]
    extra = rng.sample(range(1, n + 1), 2)
    edges.append(extra)
    edges = [e if rng.random() < 0.5 else e[::-1] for e in edges]
    rng.shuffle(edges)
    # keep the graph connected and valid: any order of a tree plus one edge works
    return [edges]


def _redundant_gen(rng):
    return [_redundant(rng, n) for n in (3, 5, 9, 20)] + [_redundant(rng, 1000)]


def _ladder_words(rng, n, length, alpha):
    words = {"".join(rng.choice(alpha) for _ in range(length)) for _ in range(n)}
    return sorted(words)


def _ladder(rng, n, length, alpha):
    words = _ladder_words(rng, n, length, alpha)
    begin = "".join(rng.choice(alpha) for _ in range(length))
    end = rng.choice(words)
    rng.shuffle(words)
    return [begin, end, words]


PROBLEMS = [
    P(80, "Number of Islands", "Medium", "numIslands",
      r'''
`grid` is a map made of the strings `"1"` (land) and `"0"` (water). An island is a group of land cells connected horizontally or vertically (diagonals do not connect). Everything outside the grid counts as water.

Return the number of islands.

## Examples

```
Input:  grid = [["0","1","1","1","0"],
                ["0","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
Output: 1

Input:  grid = [["1","0"],["0","1"]]
Output: 2
```

## Constraints

- `1 <= rows, cols <= 60`
- `grid[i][j]` is `"0"` or `"1"`.

## Hints

- Scan the grid. When you meet unvisited land, count one island and flood-fill all of it (DFS or BFS).
''',
      r'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass
''',
      r'''
class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        seen = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    stack = [(r, c)]
                    seen.add((r, c))
                    while stack:
                        x, y = stack.pop()
                        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                stack.append((nx, ny))
        return count
''',
      [([[["0", "1", "1", "1", "0"], ["0", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]], 1),
       ([[["1", "1", "0", "0", "1"], ["1", "1", "0", "0", "1"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]], 4),
       ([[["0"]]], 0), ([[["1"]]], 1), ([[["1", "0", "1"]]], 2), ([[["1"], ["0"], ["1"]]], 2),
       ([[["1", "1"], ["1", "1"]]], 1), ([[["1", "0"], ["0", "1"]]], 2)],
      gen=_islands_gen,
      small=lambda rng: [_grid(rng, rng.randint(1, 4), rng.randint(1, 4), 0.5)],
      brute=r'''
class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        parent = {(r, c): (r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "1"}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for (r, c) in list(parent):
            for n in ((r + 1, c), (r, c + 1)):
                if n in parent:
                    parent[find((r, c))] = find(n)
        return len({find(x) for x in parent})
'''),

    P(81, "Max Area of Island", "Medium", "maxAreaOfIsland",
      r'''
`grid` is a map of `1` (land) and `0` (water). An island is a group of land cells connected horizontally or vertically. Its area is the number of cells it contains.

Return the largest island area. If there is no land, return `0`.

## Examples

```
Input:  grid = [[0,1,1,0,1],
                [1,0,1,0,1],
                [0,1,1,0,1],
                [0,1,0,0,1]]
Output: 6

Input:  grid = [[0,0,0]]
Output: 0
```

## Constraints

- `1 <= rows, cols <= 60`
- `grid[i][j]` is `0` or `1`.

## Hints

- Flood-fill each island and count the cells you visit; keep the maximum.
''',
      r'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pass
''',
      r'''
class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        seen = set()
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    stack, area = [(r, c)], 0
                    while stack:
                        x, y = stack.pop()
                        area += 1
                        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                stack.append((nx, ny))
                    best = max(best, area)
        return best
''',
      [([[[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]], 6), ([[[0, 0, 0]]], 0), ([[[1]]], 1),
       ([[[1, 1], [1, 1]]], 4), ([[[1, 0], [0, 1]]], 1), ([[[1, 1, 0], [0, 1, 1]]], 4)],
      gen=_area_gen,
      small=lambda rng: [_igrid(rng, rng.randint(1, 4), rng.randint(1, 4), 0.55)],
      brute=r'''
class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        label = {}
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in label:
                    comp, frontier = {(r, c)}, [(r, c)]
                    while frontier:
                        nxt = []
                        for x, y in frontier:
                            for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                                if n not in comp and 0 <= n[0] < rows and 0 <= n[1] < cols and grid[n[0]][n[1]] == 1:
                                    comp.add(n)
                                    nxt.append(n)
                        frontier = nxt
                    for cell in comp:
                        label[cell] = 1
                    best = max(best, len(comp))
        return best
'''),

    P(82, "Clone Graph", "Medium", "cloneGraph",
      r'''
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
''',
      r'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        pass
''',
      r'''
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        copies = {node: Node(node.val)}
        stack = [node]
        while stack:
            cur = stack.pop()
            for n in cur.neighbors:
                if n not in copies:
                    copies[n] = Node(n.val)
                    stack.append(n)
                copies[cur].neighbors.append(copies[n])
        return copies[node]
''',
      [([x], x) for x in [[[2, 4], [1, 3], [2, 4], [1, 3]], [[]], [], [[2], [1]], [[2, 3], [1, 3], [1, 2]],
                          [[2], [1, 3], [2]]]],
      arg_types=["graph"], return_type="graph",
      checker=r'''
from leet.structures import graph_to


def check(args, got, expected, inputs):
    originals = set()
    stack = [inputs[0]] if inputs[0] is not None else []
    while stack:
        node = stack.pop()
        if id(node) not in originals:
            originals.add(id(node))
            stack.extend(node.neighbors)
    if graph_to(inputs[0]) != args[0]:
        return "the original graph was modified"
    if graph_to(got) != args[0]:
        return "the clone does not have the same values and connections as the original"
    stack, seen = ([got] if got is not None else []), set()
    while stack:
        node = stack.pop()
        if id(node) in seen:
            continue
        seen.add(id(node))
        if id(node) in originals:
            return "the clone reuses nodes of the original graph"
        stack.extend(node.neighbors)
    return True
''',
      gen=_clone_gen,
      small=lambda rng: [_connected(rng, rng.randint(1, 7), rng.randint(0, 6))],
      brute=r'''
from collections import deque


class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        order, q, seen = [], deque([node]), {node}
        while q:
            cur = q.popleft()
            order.append(cur)
            for n in cur.neighbors:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        copy = {n: Node(n.val) for n in order}
        for n in order:
            copy[n].neighbors = [copy[m] for m in n.neighbors]
        return copy[node]
'''),

    P(83, "Walls and Gates", "Medium", "wallsAndGates",
      r'''
`rooms` is a grid where each cell is one of:

- `-1`: a wall you cannot pass,
- `0`: a gate,
- `2147483647` (called INF): an empty room.

Fill every empty room with the number of steps to its nearest gate (moving up, down, left or right through non-wall cells). If a room cannot reach any gate, leave it as `2147483647`. Modify `rooms` in place; return nothing.

## Examples

```
Input:  [[INF, -1,  0, INF],
         [INF, INF, INF, -1],
         [INF, -1, INF, -1],
         [  0, -1, INF, INF]]
Output: [[3, -1, 0, 1],
         [2,  2, 1, -1],
         [1, -1, 2, -1],
         [0, -1, 3, 4]]
```

## Constraints

- `1 <= rows, cols <= 60`
- Cells are `-1`, `0` or `2147483647`.

## Hints

- Start a breadth-first search from all gates at the same time. The first time the search reaches a room is its shortest distance.
''',
      r'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        pass
''',
      r'''
from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        rows, cols = len(rooms), len(rooms[0])
        q = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        while q:
            r, c = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
''',
      [([[[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]],
        [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
       ([[[-1]]], [[-1]]), ([[[0]]], [[0]]), ([[[INF]]], [[INF]]), ([[[0, INF]]], [[0, 1]]),
       ([[[0, INF, INF], [INF, -1, INF], [INF, INF, 0]]], [[0, 1, 2], [1, -1, 1], [2, 1, 0]]),
       ([[[INF, -1], [-1, 0]]], [[INF, -1], [-1, 0]])],
      inplace=0,
      gen=_rooms_gen,
      small=lambda rng: [_rooms(rng, rng.randint(1, 4), rng.randint(1, 4))],
      brute=r'''
from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        rows, cols = len(rooms), len(rooms[0])
        original = [row[:] for row in rooms]
        for r in range(rows):
            for c in range(cols):
                if original[r][c] != 2147483647:
                    continue
                dist, q = {(r, c): 0}, deque([(r, c)])
                found = None
                while q and found is None:
                    x, y = q.popleft()
                    if original[x][y] == 0:
                        found = dist[(x, y)]
                        break
                    for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if n not in dist and 0 <= n[0] < rows and 0 <= n[1] < cols and original[n[0]][n[1]] != -1:
                            dist[n] = dist[(x, y)] + 1
                            q.append(n)
                if found is not None:
                    rooms[r][c] = found
'''),

    P(84, "Rotting Oranges", "Medium", "orangesRotting",
      r'''
`grid` describes a box of oranges: `0` is an empty cell, `1` is a fresh orange, and `2` is a rotten orange.

Every minute, each fresh orange that is directly next to a rotten one (up, down, left or right) becomes rotten.

Return the number of minutes until no fresh orange is left. If that never happens, return `-1`.

## Examples

```
Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
```

## Constraints

- `1 <= rows, cols <= 60`
- `grid[i][j]` is `0`, `1` or `2`.

## Hints

- Spread rot one minute at a time with a breadth-first search that starts from every rotten orange.
- At the end, check whether any fresh orange remains.
''',
      r'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass
''',
      r'''
from collections import deque


class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while q and fresh:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
        return -1 if fresh else minutes
''',
      [([[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], 4), ([[[2, 1, 1], [0, 1, 1], [1, 0, 1]]], -1), ([[[0, 2]]], 0),
       ([[[0]]], 0), ([[[1]]], -1), ([[[2]]], 0), ([[[2, 1, 1], [1, 1, 1], [0, 1, 2]]], 2), ([[[1, 2]]], 1),
       ([[[2, 0, 1]]], -1)],
      gen=_oranges_gen,
      small=lambda rng: [_oranges(rng, rng.randint(1, 4), rng.randint(1, 4))],
      brute=r'''
class Solution:
    def orangesRotting(self, grid):
        g = [row[:] for row in grid]
        rows, cols = len(g), len(g[0])
        minutes = 0
        while any(1 in row for row in g):
            new = [row[:] for row in g]
            changed = False
            for r in range(rows):
                for c in range(cols):
                    if g[r][c] == 1 and any(
                        0 <= r + dr < rows and 0 <= c + dc < cols and g[r + dr][c + dc] == 2
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                    ):
                        new[r][c] = 2
                        changed = True
            if not changed:
                return -1
            g = new
            minutes += 1
        return minutes
'''),

    P(85, "Pacific Atlantic Water Flow", "Medium", "pacificAtlantic",
      r'''
`heights[r][c]` is the height of a cell on an island. The Pacific Ocean touches the top and left edges of the grid, and the Atlantic Ocean touches the bottom and right edges.

Rain water can flow from a cell to a neighbouring cell (up, down, left or right) whose height is less than or equal to its own. Water on an edge cell can flow into the ocean touching that edge.

Return every cell `[r, c]` from which water can reach both oceans. The cells may be in any order.

## Examples

```
Input:  heights = [[1,2,2,3,5],
                   [3,2,3,4,4],
                   [2,4,5,3,1],
                   [6,7,1,4,5],
                   [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Constraints

- `1 <= rows, cols <= 30`
- `0 <= heights[r][c] <= 100`

## Hints

- Run the search backwards: from each ocean's edge, climb to neighbours that are the same height or higher. The answer is the intersection of the two reachable sets.
''',
      r'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])

        def reach(starts):
            seen = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return seen

        pacific = reach([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
        atlantic = reach([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)])
        return [list(cell) for cell in pacific & atlantic]
''',
      [([[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
       ([[[1]]], [[0, 0]]), ([[[1, 1], [1, 1]]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
       ([[[2, 1], [1, 2]]], [[0, 0], [0, 1], [1, 0], [1, 1]]), ([[[1, 2, 3]]], [[0, 0], [0, 1], [0, 2]])],
      compare="unordered",
      gen=_pacific_gen,
      small=lambda rng: [_heights(rng, rng.randint(1, 4), rng.randint(1, 4))],
      brute=r'''
from collections import deque


class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        out = []
        for r in range(rows):
            for c in range(cols):
                seen, q = {(r, c)}, deque([(r, c)])
                pac = atl = False
                while q:
                    x, y = q.popleft()
                    pac = pac or x == 0 or y == 0
                    atl = atl or x == rows - 1 or y == cols - 1
                    for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if n not in seen and 0 <= n[0] < rows and 0 <= n[1] < cols and heights[n[0]][n[1]] <= heights[x][y]:
                            seen.add(n)
                            q.append(n)
                if pac and atl:
                    out.append([r, c])
        return out
'''),

    P(86, "Surrounded Regions", "Medium", "solve",
      r'''
`board` is a grid of `"X"` and `"O"`. A region of connected `"O"` cells (connected horizontally or vertically) is surrounded if none of its cells lies on the border of the board. Turn every surrounded region of `"O"` into `"X"`.

Modify `board` in place; return nothing.

## Examples

```
Input:  [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
```

## Constraints

- `1 <= rows, cols <= 60`
- `board[i][j]` is `"X"` or `"O"`.

## Hints

- Instead of finding surrounded regions, find the safe ones: mark every `"O"` reachable from a border `"O"`. Everything else becomes `"X"`.
''',
      r'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass
''',
      r'''
class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        stack = [(r, c) for r in range(rows) for c in range(cols)
                 if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == "O"]
        safe = set(stack)
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in safe:
                    safe.add((nr, nc))
                    stack.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
''',
      [([[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]],
        [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
       ([[["X"]]], [["X"]]), ([[["O"]]], [["O"]]), ([[["O", "O"], ["O", "O"]]], [["O", "O"], ["O", "O"]]),
       ([[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]], [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]),
       ([[["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]], [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]),
       ([[["X", "X", "X", "X", "X"], ["X", "O", "O", "O", "X"], ["X", "O", "X", "O", "X"], ["X", "O", "O", "O", "X"],
          ["X", "X", "X", "X", "X"]]],
        [["X"] * 5 for _ in range(5)])],
      inplace=0,
      gen=_xo_gen,
      small=lambda rng: [_xo(rng, rng.randint(1, 5), rng.randint(1, 5))],
      brute=r'''
class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        orig = [row[:] for row in board]

        def escapes(r, c):
            seen, stack = {(r, c)}, [(r, c)]
            while stack:
                x, y = stack.pop()
                if x in (0, rows - 1) or y in (0, cols - 1):
                    return True
                for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if n not in seen and orig[n[0]][n[1]] == "O":
                        seen.add(n)
                        stack.append(n)
            return False

        for r in range(rows):
            for c in range(cols):
                if orig[r][c] == "O" and not escapes(r, c):
                    board[r][c] = "X"
'''),

    P(87, "Course Schedule", "Medium", "canFinish",
      r'''
You must take `numCourses` courses, labelled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means you must take course `b` before course `a`.

Return `True` if it is possible to finish all courses, otherwise `False` (which happens when the prerequisites contain a cycle).

## Examples

```
Input:  numCourses = 2, prerequisites = [[0, 1]]
Output: True

Input:  numCourses = 2, prerequisites = [[0, 1], [1, 0]]
Output: False
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= len(prerequisites) <= 3000`
- All pairs are distinct.

## Hints

- Model courses as nodes and prerequisites as directed edges. The question is whether the graph has a cycle.
- Topological sorting (repeatedly take courses with no remaining prerequisites) detects cycles.
''',
      r'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass
''',
      r'''
from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        indeg = [0] * numCourses
        after = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            after[b].append(a)
            indeg[a] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        done = 0
        while q:
            c = q.popleft()
            done += 1
            for nxt in after[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return done == numCourses
''',
      [([2, [[0, 1]]], True), ([2, [[0, 1], [1, 0]]], False), ([1, []], True), ([3, [[1, 0], [2, 1]]], True),
       ([3, [[1, 0], [0, 2], [2, 1]]], False), ([4, [[1, 0], [2, 0], [3, 1], [3, 2]]], True), ([2, []], True),
       ([3, [[0, 0]]], False), ([5, [[1, 0], [2, 1], [3, 2], [4, 3], [1, 4]]], False)],
      gen=_courses_gen, small=_courses_small,
      brute=r'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        remaining = set(range(numCourses))
        edges = [tuple(e) for e in prerequisites]
        while remaining:
            free = [c for c in remaining if not any(a == c and b in remaining for a, b in edges)]
            if not free:
                return False
            remaining -= set(free)
        return True
'''),

    P(88, "Course Schedule II", "Medium", "findOrder",
      r'''
You must take `numCourses` courses, labelled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means you must take course `b` before course `a`.

Return an order in which you can take all the courses. If several orders work, return any one of them. If it is impossible (there is a cycle), return an empty list.

## Examples

```
Input:  numCourses = 2, prerequisites = [[1, 0]]
Output: [0, 1]

Input:  numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3]      # [0, 2, 1, 3] is also accepted
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= len(prerequisites) <= 3000`
- All pairs are distinct.

## Hints

- The order is a topological sort. If your sort cannot include every course, there is a cycle.
''',
      r'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass
''',
      r'''
from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        indeg = [0] * numCourses
        after = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            after[b].append(a)
            indeg[a] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for nxt in after[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == numCourses else []
''',
      [([2, [[1, 0]]], [0, 1]), ([4, [[1, 0], [2, 0], [3, 1], [3, 2]]], [0, 1, 2, 3]), ([1, []], [0]),
       ([2, [[0, 1], [1, 0]]], []), ([3, []], [0, 1, 2]), ([3, [[0, 1], [1, 2]]], [2, 1, 0]),
       ([3, [[1, 0], [2, 1], [0, 2]]], [])],
      checker=r'''
def check(args, got, expected, inputs):
    n, prereqs = args
    if not isinstance(got, list):
        return "return a list"
    if expected == []:
        return got == [] or "there is a cycle, so the answer must be an empty list"
    if sorted(got) != list(range(n)):
        return "the order must contain every course exactly once"
    pos = {c: i for i, c in enumerate(got)}
    for a, b in prereqs:
        if pos[b] > pos[a]:
            return f"course {b} must come before course {a}"
    return True
''',
      gen=_courses_gen, small=_courses_small,
      brute=r'''
class Solution:
    def findOrder(self, numCourses, prerequisites):
        remaining = set(range(numCourses))
        edges = [tuple(e) for e in prerequisites]
        order = []
        while remaining:
            free = sorted(c for c in remaining if not any(a == c and b in remaining for a, b in edges))
            if not free:
                return []
            order += free
            remaining -= set(free)
        return order
'''),

    P(89, "Graph Valid Tree", "Medium", "validTree",
      r'''
A graph has `n` nodes labelled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]`.

Return `True` if the edges form a valid tree (connected, with no cycles), otherwise `False`.

## Examples

```
Input:  n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: True

Input:  n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: False
```

## Constraints

- `1 <= n <= 3000`
- `0 <= len(edges) <= 3000`
- There are no duplicate edges and no self-loops.

## Hints

- A tree on `n` nodes has exactly `n - 1` edges. If that holds, you only need to check one more thing.
''',
      r'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass
''',
      r'''
class Solution:
    def validTree(self, n, edges):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return len(edges) == n - 1
''',
      [([5, [[0, 1], [0, 2], [0, 3], [1, 4]]], True), ([5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]], False),
       ([1, []], True), ([2, []], False), ([2, [[0, 1]]], True), ([3, [[0, 1], [1, 2], [2, 0]]], False),
       ([4, [[0, 1], [2, 3]]], False), ([4, [[0, 1], [0, 2], [0, 3]]], True)],
      gen=_valid_tree_gen, small=_tree_small,
      brute=r'''
class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen, stack = {0}, [0]
        while stack:
            for m in adj[stack.pop()]:
                if m not in seen:
                    seen.add(m)
                    stack.append(m)
        return len(seen) == n
'''),

    P(90, "Number of Connected Components in an Undirected Graph", "Medium", "countComponents",
      r'''
A graph has `n` nodes labelled `0` to `n - 1` and a list of undirected `edges`, where `edges[i] = [a, b]`.

Return the number of connected components: groups of nodes that can reach each other through edges.

## Examples

```
Input:  n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2

Input:  n = 3, edges = []
Output: 3
```

## Constraints

- `1 <= n <= 5000`
- `0 <= len(edges) <= 5000`
- There are no duplicate edges and no self-loops.

## Hints

- Union-find: start with `n` components and subtract one every time an edge joins two different components.
''',
      r'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass
''',
      r'''
class Solution:
    def countComponents(self, n, edges):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        count = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                count -= 1
        return count
''',
      [([5, [[0, 1], [1, 2], [3, 4]]], 2), ([5, [[0, 1], [1, 2], [2, 3], [3, 4]]], 1), ([1, []], 1), ([3, []], 3),
       ([4, [[0, 1], [2, 3]]], 2), ([6, [[0, 1], [1, 2], [0, 2], [3, 4]]], 3)],
      gen=_components_gen,
      small=lambda rng: (lambda n: [n, _rand_edges(rng, n, rng.randint(0, min(6, n * (n - 1) // 2)))])(rng.randint(1, 7)),
      brute=r'''
class Solution:
    def countComponents(self, n, edges):
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen, comps = set(), 0
        for s in range(n):
            if s in seen:
                continue
            comps += 1
            seen.add(s)
            stack = [s]
            while stack:
                for m in adj[stack.pop()]:
                    if m not in seen:
                        seen.add(m)
                        stack.append(m)
        return comps
'''),

    P(91, "Redundant Connection", "Medium", "findRedundantConnection",
      r'''
A connected, undirected graph with nodes labelled `1` to `n` was a tree, and then one extra edge was added. You are given the resulting list of `edges`.

Return an edge that can be removed so that the remaining graph is a tree again. If several edges qualify, return the one that appears last in `edges`.

## Examples

```
Input:  edges = [[1, 2], [1, 3], [2, 3]]
Output: [2, 3]

Input:  edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
Output: [1, 4]
```

## Constraints

- `3 <= n <= 1000`, and `len(edges) == n`
- `1 <= a < b <= n` is not guaranteed; an edge may be written in either direction.
- There are no repeated edges.

## Hints

- Add the edges one by one with union-find. The first edge whose endpoints are already connected closes the cycle.
''',
      r'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass
''',
      r'''
class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]
            parent[ra] = rb
''',
      [([[[1, 2], [1, 3], [2, 3]]], [2, 3]), ([[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]], [1, 4]),
       ([[[1, 2], [2, 3], [1, 3]]], [1, 3]), ([[[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]], [1, 3]),
       ([[[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]], [2, 5])],
      gen=_redundant_gen,
      small=lambda rng: _redundant(rng, rng.randint(3, 8)),
      brute=r'''
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        def is_tree(es):
            adj = {i: [] for i in range(1, n + 1)}
            for a, b in es:
                adj[a].append(b)
                adj[b].append(a)
            seen, stack = {1}, [1]
            while stack:
                for m in adj[stack.pop()]:
                    if m not in seen:
                        seen.add(m)
                        stack.append(m)
            return len(seen) == n

        for i in range(n - 1, -1, -1):
            if is_tree(edges[:i] + edges[i + 1:]):
                return edges[i]
'''),

    P(92, "Word Ladder", "Hard", "ladderLength",
      r'''
You are given a `beginWord`, an `endWord` and a list `wordList`. A transformation changes exactly one letter at a time, and every word you pass through (except `beginWord`) must be in `wordList`.

Return the number of words in the shortest sequence from `beginWord` to `endWord`, counting both ends. If no sequence exists, return `0`. `beginWord` does not need to be in `wordList`.

## Examples

```
Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5          # hit -> hot -> dot -> dog -> cog

Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0          # "cog" is not in the list
```

## Constraints

- `1 <= len(beginWord) <= 10`, and `len(endWord) == len(beginWord)`
- `1 <= len(wordList) <= 3000`, and every word has the same length
- Words consist of lowercase letters; the words in `wordList` are unique.

## Hints

- Breadth-first search gives the shortest sequence.
- To find neighbours quickly, group words by patterns such as `h*t`, `*ot`, `ho*`.
''',
      r'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass
''',
      r'''
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        groups = defaultdict(list)
        for w in set(wordList) | {beginWord}:
            for i in range(len(w)):
                groups[w[:i] + "*" + w[i + 1:]].append(w)
        seen = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for i in range(len(w)):
                for n in groups[w[:i] + "*" + w[i + 1:]]:
                    if n not in seen:
                        seen.add(n)
                        q.append((n, d + 1))
        return 0
''',
      [(["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], 5), (["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], 0),
       (["a", "c", ["a", "b", "c"]], 2), (["cat", "dog", ["bat", "cot", "cog", "dog"]], 4), (["hot", "dog", ["hot", "dog"]], 0),
       (["hit", "hot", ["hot"]], 2), (["aa", "bb", ["ab", "bb"]], 3)],
      gen=lambda rng: [_ladder(rng, n, ln, "abc") for n, ln in ((6, 3), (10, 3), (15, 4), (20, 4))]
      + [_ladder(rng, 3000, 6, "abcd"), _ladder(rng, 3000, 5, "abc")],
      small=lambda rng: _ladder(rng, rng.randint(2, 8), 3, "ab"),
      brute=r'''
from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        dist = {beginWord: 1}
        q = deque([beginWord])
        while q:
            w = q.popleft()
            for other in words | {beginWord}:
                if other not in dist and sum(a != b for a, b in zip(w, other)) == 1:
                    dist[other] = dist[w] + 1
                    q.append(other)
        return dist.get(endWord, 0)
'''),
]
