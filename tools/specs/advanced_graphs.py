from spec import P

CATEGORY = "advanced-graphs"


def _itinerary(rng, steps, airports):
    walk = ["JFK"]
    for _ in range(steps):
        nxt = rng.choice(airports)
        while nxt == walk[-1] and len(airports) > 1:
            nxt = rng.choice(airports)
        walk.append(nxt)
    tickets = [[a, b] for a, b in zip(walk, walk[1:])]
    rng.shuffle(tickets)
    return [tickets]


def _points(rng, n, span):
    seen = set()
    while len(seen) < n:
        seen.add((rng.randint(-span, span), rng.randint(-span, span)))
    return [[x, y] for x, y in sorted(seen, key=lambda _: rng.random())]


def _delay(rng, n, m):
    edges = {}
    while len(edges) < m and len(edges) < n * (n - 1):
        a, b = rng.sample(range(1, n + 1), 2)
        edges[(a, b)] = rng.randint(1, 20)
    return [[a, b, w] for (a, b), w in edges.items()], n, rng.randint(1, n)


def _delay_case(rng, n, m):
    times, n, k = _delay(rng, n, m)
    return [times, n, k]


def _swim(rng, n):
    cells = list(range(n * n))
    rng.shuffle(cells)
    return [[cells[r * n:(r + 1) * n] for r in range(n)]]


def _alien(rng, letters, n_words, corrupt):
    order = list(letters)
    rng.shuffle(order)
    rank = {c: i for i, c in enumerate(order)}
    words = {"".join(rng.choice(letters) for _ in range(rng.randint(1, 4))) for _ in range(n_words)}
    words = sorted(words, key=lambda w: [rank[c] for c in w])
    if corrupt and len(words) > 2:
        i = rng.randrange(len(words) - 1)
        words[i], words[i + 1] = words[i + 1], words[i]
    return [words]


def _alien_gen(rng):
    out = [_alien(rng, "abcd", 6, False) for _ in range(3)]
    out += [_alien(rng, "abcdef", 12, False) for _ in range(2)]
    out += [_alien(rng, "abcde", 8, True) for _ in range(3)]
    out.append(_alien(rng, "abcdefghijklmnopqrstuvwxyz", 300, False))
    return out


def _flights(rng, n, m, k):
    edges = {}
    while len(edges) < m and len(edges) < n * (n - 1):
        a, b = rng.sample(range(n), 2)
        edges[(a, b)] = rng.randint(1, 300)
    src, dst = rng.sample(range(n), 2)
    return [n, [[a, b, w] for (a, b), w in edges.items()], src, dst, k]


PROBLEMS = [
    P(93, "Reconstruct Itinerary", "Hard", "findItinerary",
      r'''
`tickets[i] = [from, to]` is an airline ticket for a flight between two airports (given as three-letter codes). Rebuild the trip of a traveller who starts at `"JFK"` and uses every ticket exactly once.

Return the itinerary as the list of airports in visiting order. If several valid itineraries exist, return the one that is smallest in lexical order (compare the airports one by one, as strings). A valid itinerary is guaranteed to exist.

## Examples

```
Input:  tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input:  tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

## Constraints

- `1 <= len(tickets) <= 2000`
- Airport codes are three uppercase letters.
- `from != to` for every ticket, and tickets may repeat.

## Hints

- This is an Eulerian path. Hierholzer's algorithm builds it with a DFS that always takes the smallest destination first and appends airports on the way back.
''',
      r'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass
''',
      r'''
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        route, stack = [], ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
''',
      [([[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
       ([[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]],
        ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
       ([[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]], ["JFK", "NRT", "JFK", "KUL"]),
       ([[["JFK", "AAA"]]], ["JFK", "AAA"]), ([[["JFK", "AAA"], ["AAA", "JFK"]]], ["JFK", "AAA", "JFK"]),
       ([[["JFK", "BBB"], ["JFK", "AAA"], ["AAA", "JFK"]]], ["JFK", "AAA", "JFK", "BBB"])],
      gen=lambda rng: [_itinerary(rng, s, a) for s, a in ((3, ["JFK", "AAA"]), (6, ["JFK", "AAA", "BBB"]),
                                                        (10, ["JFK", "AAA", "BBB", "CCC"]), (12, ["JFK", "AAA", "BBB"]))]
      + [_itinerary(rng, 2000, ["JFK", "AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"])],
      small=lambda rng: _itinerary(rng, rng.randint(1, 8), ["JFK", "AAA", "BBB"]),
      brute=r'''
class Solution:
    def findItinerary(self, tickets):
        tickets = sorted(tickets)
        used = [False] * len(tickets)

        def go(path):
            if len(path) == len(tickets) + 1:
                return path
            for i, (a, b) in enumerate(tickets):
                if not used[i] and a == path[-1]:
                    used[i] = True
                    res = go(path + [b])
                    if res:
                        return res
                    used[i] = False
            return None

        return go(["JFK"])
'''),

    P(94, "Min Cost to Connect All Points", "Medium", "minCostConnectPoints",
      r'''
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
''',
      r'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass
''',
      r'''
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        best = [float("inf")] * n
        used = [False] * n
        best[0] = 0
        total = 0
        for _ in range(n):
            u = min((i for i in range(n) if not used[i]), key=best.__getitem__)
            used[u] = True
            total += best[u]
            ux, uy = points[u]
            for v in range(n):
                if not used[v]:
                    d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                    if d < best[v]:
                        best[v] = d
        return total
''',
      [([[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]], 20), ([[[3, 12], [-2, 5], [-4, 1]]], 18), ([[[0, 0]]], 0),
       ([[[0, 0], [1, 1]]], 2), ([[[0, 0], [1, 1], [1, 0], [-1, 1]]], 4),
       ([[[2, -3], [-17, -8], [13, 8], [-17, -15]]], 53)],
      gen=lambda rng: [[_points(rng, n, 20)] for n in (2, 4, 7, 12)] + [[_points(rng, 800, 1000000)]],
      small=lambda rng: [_points(rng, rng.randint(1, 7), 6)],
      brute=r'''
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = sorted((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j)
                       for i in range(n) for j in range(i + 1, n))
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        total = 0
        for d, i, j in edges:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[ri] = rj
                total += d
        return total
'''),

    P(95, "Network Delay Time", "Medium", "networkDelayTime",
      r'''
A network has `n` nodes labelled `1` to `n`. `times[i] = [u, v, w]` means a signal sent from node `u` reaches node `v` after `w` time units (a directed connection).

A signal is sent from node `k`. Return the minimum time until all nodes have received it, or `-1` if some node can never receive it.

## Examples

```
Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Input:  times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## Constraints

- `1 <= k <= n <= 1000`
- `0 <= len(times) <= 5000`
- `1 <= w <= 100`, and each `(u, v)` pair appears at most once

## Hints

- Dijkstra's algorithm gives the shortest time to every node. The answer is the largest of those times.
''',
      r'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass
''',
      r'''
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return max(dist.values()) if len(dist) == n else -1
''',
      [([[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2], 2), ([[[1, 2, 1]], 2, 1], 1), ([[[1, 2, 1]], 2, 2], -1),
       ([[[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1], 3), ([[[1, 2, 1], [2, 1, 3]], 2, 2], 3),
       ([[[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1], 2), ([[], 1, 1], 0)],
      gen=lambda rng: [_delay_case(rng, n, m) for n, m in ((3, 3), (5, 8), (8, 20), (10, 15))]
      + [_delay_case(rng, 1000, 5000), _delay_case(rng, 1000, 1500)],
      small=lambda rng: _delay_case(rng, (n := rng.randint(1, 6)), rng.randint(0, n * 2)),
      brute=r'''
class Solution:
    def networkDelayTime(self, times, n, k):
        inf = float("inf")
        dist = [inf] * (n + 1)
        dist[k] = 0
        for _ in range(n):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        worst = max(dist[1:])
        return -1 if worst == inf else worst
'''),

    P(96, "Swim in Rising Water", "Hard", "swimInWater",
      r'''
`grid` is an `n x n` grid of distinct integers from `0` to `n * n - 1`; `grid[r][c]` is the elevation of a square. At time `t` the water level is `t` everywhere, and you can stand on (and move between) squares whose elevation is at most `t`. Swimming between adjacent squares (up, down, left, right) takes no time.

You start at the top-left square at time `0`. Return the least time at which you can reach the bottom-right square.

## Examples

```
Input:  grid = [[0, 2], [1, 3]]
Output: 3

Input:  grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
```

## Constraints

- `1 <= n <= 40`
- All values in `grid` are distinct.

## Hints

- You are looking for the path whose highest square is as low as possible. A Dijkstra-style search with a min-heap on elevation does it.
''',
      r'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pass
''',
      r'''
import heapq


class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) == (n - 1, n - 1):
                return t
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
''',
      [([[[0, 2], [1, 3]]], 3), ([[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20],
                                  [10, 9, 8, 7, 6]]], 16), ([[[0]]], 0), ([[[0, 1], [2, 3]]], 3), ([[[3, 2], [0, 1]]], 3),
       ([[[0, 3], [1, 2]]], 2)],
      gen=lambda rng: [_swim(rng, n) for n in (2, 3, 4, 6, 10, 40)],
      small=lambda rng: _swim(rng, rng.randint(1, 4)),
      brute=r'''
from collections import deque


class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        t = grid[0][0]
        while True:
            seen, q = {(0, 0)}, deque([(0, 0)])
            while q:
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] <= t:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            if (n - 1, n - 1) in seen:
                return t
            t += 1
'''),

    P(97, "Alien Dictionary", "Hard", "foreignDictionary",
      r'''
A language uses the lowercase English letters but in an unknown alphabetical order. You are given a list `words` that is sorted according to the rules of that language (compare words letter by letter, and a shorter word that is a prefix of a longer one comes first).

Return a string containing the distinct letters of `words` in a valid order for the language. If several orders are valid, return any of them. If the list cannot be sorted under any order (for example `["abc", "ab"]` or a contradiction), return an empty string `""`.

## Examples

```
Input:  words = ["z", "o"]
Output: "zo"

Input:  words = ["hrn", "hrf", "er", "enn", "rfnn"]
Output: "hernf"     # other valid orders are accepted too

Input:  words = ["abc", "ab"]
Output: ""
```

## Constraints

- `1 <= len(words) <= 300`
- `1 <= len(words[i]) <= 100`
- `words[i]` consists of lowercase English letters.

## Hints

- Compare each pair of neighbouring words: the first position where they differ gives one ordering rule `a before b`.
- Topologically sort the letters using those rules. A cycle means there is no valid order.
''',
      r'''
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        pass
''',
      r'''
from collections import deque


class Solution:
    def foreignDictionary(self, words):
        after = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in after}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a.startswith(b):
                return ""
            for x, y in zip(a, b):
                if x != y:
                    if y not in after[x]:
                        after[x].add(y)
                        indeg[y] += 1
                    break
        q = deque(c for c in sorted(indeg) if indeg[c] == 0)
        out = []
        while q:
            c = q.popleft()
            out.append(c)
            for n in sorted(after[c]):
                indeg[n] -= 1
                if indeg[n] == 0:
                    q.append(n)
        return "".join(out) if len(out) == len(after) else ""
''',
      [([["z", "o"]], "zo"), ([["hrn", "hrf", "er", "enn", "rfnn"]], "hernf"), ([["wrt", "wrf", "er", "ett", "rftt"]], "wertf"),
       ([["abc", "ab"]], ""), ([["a", "b", "a"]], ""), ([["z", "x"]], "zx"), ([["z", "x", "z"]], ""),
       ([["a"]], "a"), ([["ab", "ac"]], "abc")],
      checker=r'''
def check(args, got, expected, inputs):
    words = args[0]
    if not isinstance(got, str):
        return "return a string"
    if expected == "":
        return got == "" or "no valid order exists, expected an empty string"
    letters = {c for w in words for c in w}
    if len(got) != len(set(got)) or set(got) != letters:
        return "the result must contain each letter of the words exactly once"
    rank = {c: i for i, c in enumerate(got)}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if rank[x] > rank[y]:
                    return f"'{x}' must come before '{y}' because of the words {a!r} and {b!r}"
                break
    return True
''',
      gen=_alien_gen,
      small=lambda rng: _alien(rng, "abc", rng.randint(2, 5), rng.random() < 0.3),
      brute=r'''
from itertools import permutations


class Solution:
    def foreignDictionary(self, words):
        letters = sorted({c for w in words for c in w})
        for perm in permutations(letters):
            rank = {c: i for i, c in enumerate(perm)}
            keys = [[rank[c] for c in w] for w in words]
            if keys == sorted(keys):
                return "".join(perm)
        return ""
'''),

    P(98, "Cheapest Flights Within K Stops", "Medium", "findCheapestPrice",
      r'''
There are `n` cities labelled `0` to `n - 1`. `flights[i] = [from, to, price]` is a one-way flight.

Return the cheapest price to travel from city `src` to city `dst` using at most `k` stops (cities visited in between, so at most `k + 1` flights). If there is no such route, return `-1`.

## Examples

```
Input:  n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700

Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
```

## Constraints

- `1 <= n <= 500`
- `0 <= len(flights) <= 3000`
- `0 <= src, dst, k < n`, and `src != dst`
- `1 <= price <= 300`; there is at most one flight per ordered pair of cities.

## Hints

- A plain Dijkstra can pick a cheap path that uses too many stops. Track the number of stops in the state, or run Bellman-Ford for exactly `k + 1` rounds.
''',
      r'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pass
''',
      r'''
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        best = {}
        heap = [(0, src, 0)]
        while heap:
            cost, u, used = heapq.heappop(heap)
            if u == dst:
                return cost
            if used > k or best.get((u, used), float("inf")) <= cost:
                continue
            best[(u, used)] = cost
            for v, w in graph[u]:
                heapq.heappush(heap, (cost + w, v, used + 1))
        return -1
''',
      [([4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1], 700),
       ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], 200), ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], 500),
       ([2, [[0, 1, 100]], 1, 0, 1], -1), ([3, [[0, 1, 100], [1, 2, 100]], 0, 2, 0], -1),
       ([5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2], 7),
       ([5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 3], 6)],
      gen=lambda rng: [_flights(rng, n, m, k) for n, m, k in ((4, 6, 1), (6, 12, 2), (8, 20, 3), (10, 30, 0), (10, 30, 9))]
      + [_flights(rng, 500, 3000, 5), _flights(rng, 500, 3000, 60)],
      small=lambda rng: _flights(rng, (n := rng.randint(2, 6)), rng.randint(0, n * 2), rng.randint(0, n - 1)),
      brute=r'''
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        inf = float("inf")
        dist = [inf] * n
        dist[src] = 0
        for _ in range(k + 1):
            new = dist[:]
            for u, v, w in flights:
                if dist[u] + w < new[v]:
                    new[v] = dist[u] + w
            dist = new
        return -1 if dist[dst] == inf else dist[dst]
'''),
]
