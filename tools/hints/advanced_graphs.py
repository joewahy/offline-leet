HINTS = {
    93: [
        "You must use every ticket exactly once. That is a path that uses every edge once, called an Eulerian path.",
        "Hierholzer's algorithm builds it with a depth-first search. Visit destinations in lexical order.",
        "Sort the destinations so the smallest is taken first. In the DFS, keep following unused tickets; when a node has none left, append it to the route. The final route is that list reversed.",
    ],
    94: [
        "You need to connect all the points with the smallest total wire length. This is a minimum spanning tree.",
        "Use Prim's or Kruskal's algorithm on the complete graph where each edge's weight is the Manhattan distance.",
        "Prim's: keep the best known distance from the tree to each outside point. Repeatedly add the closest outside point and update the others. That is O(n^2), which suits a complete graph.",
    ],
    95: [
        "The signal takes the fastest route to each node. Which algorithm finds shortest paths with positive weights?",
        "Dijkstra's algorithm from node `k`, using a min-heap.",
        "Pop the smallest `(time, node)`, skip it if the node is already finalized, record its time, and push its neighbours with `time + w`. The answer is the largest finalized time, or `-1` if fewer than `n` nodes were reached.",
    ],
    96: [
        "For a path, the time you need is the highest elevation along it. You want the path whose highest value is smallest.",
        "Search like Dijkstra, but instead of summing weights, take the maximum along the path.",
        "Use a min-heap of `(max_elevation_so_far, r, c)`. Pop the smallest, and for each unvisited neighbour push `max(current, neighbour_elevation)`. When you pop the bottom-right cell, that value is the answer. Binary searching the time and checking with a BFS also works.",
    ],
    97: [
        "Comparing two neighbouring words reveals at most one ordering rule between letters.",
        "Find the first position where two adjacent words differ: the letter in the first word comes before the letter in the second. These rules form a graph.",
        "Topologically sort the letters. Return an empty string if there is a cycle, and also if a longer word comes before its own prefix (like `abc` before `ab`). Include letters that appear in no rule.",
    ],
    98: [
        "A plain shortest-path search ignores the limit on stops. What extra information does each state need?",
        "Allow at most `k + 1` flights: use Bellman-Ford for `k + 1` rounds, or a heap that tracks the number of stops used.",
        "Bellman-Ford: keep a `dist` array. In each of `k + 1` rounds, relax every flight using a copy of the previous round's distances (so one round adds at most one flight). The answer is `dist[dst]`, or `-1` if it is still infinite.",
    ],
}
