HINTS = {
    80: [
        "Each island is a group of connected land cells. What should you do when you find a land cell you have not seen yet?",
        "Count one island, then flood fill from that cell to mark all the connected land as visited.",
        "Use DFS or BFS in the four directions. Mark cells visited (a set, or overwrite with `'0'`) so each cell is processed once. The total time is O(rows * cols).",
    ],
    81: [
        "It is the same flood fill as counting islands, but now you want the size of each island.",
        "While filling an island, count how many cells you visit.",
        "Take the maximum of those counts over all islands. Mark visited cells so you never count one twice.",
    ],
    82: [
        "A graph can have cycles, so you may reach the same node again. How do you avoid cloning it twice?",
        "Keep a dictionary from each original node to its clone.",
        "Traverse with DFS or BFS. When you first see a node, create its clone and store it. For each neighbour, make sure it has a clone, and append that clone to the current clone's `neighbors`.",
    ],
    83: [
        "A distance to the 'nearest gate' is a shortest path. What search finds shortest paths in an unweighted grid?",
        "Breadth-first search. Instead of starting from each empty room, start from all the gates together.",
        "Put every gate in the queue at distance 0. Pop a cell and, for each neighbour that is still `2147483647`, set it to `dist + 1` and enqueue it. Walls are never entered, and each cell is set only once.",
    ],
    84: [
        "Rot spreads one step per minute from every rotten orange at the same time.",
        "That is a multi-source BFS, processed in rounds. Each round is one minute.",
        "Start the queue with all rotten oranges and count the fresh ones. Process the queue level by level, rot the adjacent fresh oranges, and count one minute per level. If fresh oranges are left at the end, return `-1`.",
    ],
    85: [
        "Checking every cell against both oceans is slow. What if you search backwards from the oceans instead?",
        "Water flows downhill, so going backwards means moving to neighbours that are the same height or higher. Start from each ocean's border cells.",
        "Run a DFS or BFS from all Pacific border cells and another from all Atlantic border cells, collecting the cells each one reaches. The answer is the intersection of the two sets.",
    ],
    86: [
        "A region is safe if it touches the border. Which `O` cells can you identify right away?",
        "Start from the border cells that are `O` and mark every `O` connected to them as safe.",
        "After marking, every `O` that is not safe is surrounded, so turn it into `X`. Leave the safe ones as `O`.",
    ],
    87: [
        "Model courses as nodes and prerequisites as directed edges. When is it impossible to finish?",
        "It is impossible exactly when the graph has a cycle.",
        "Detect the cycle with a topological sort: repeatedly take courses with no remaining prerequisites (in-degree 0). If you can take all of them, there is no cycle. A DFS with a 'currently visiting' set also works.",
    ],
    88: [
        "This is the previous problem, but you must also output an order.",
        "A valid order is a topological ordering of the graph.",
        "Run Kahn's algorithm: start with the courses of in-degree 0, append each one to the order, and decrease the in-degree of the courses that depend on it. If the order has fewer than `numCourses` entries, return `[]`.",
    ],
    89: [
        "What two properties define a tree? How many edges does it have, and what must be true about its connectivity?",
        "A tree on `n` nodes has exactly `n - 1` edges and is connected (equivalently, it has no cycle).",
        "Check `len(edges) == n - 1` first. Then verify connectivity with a DFS from node 0, or add the edges with union-find and fail if an edge joins two nodes that are already connected.",
    ],
    90: [
        "Each connected group of nodes counts once. How do you avoid counting a group twice?",
        "Either traverse the graph and count how many times you start a new traversal, or use union-find.",
        "With union-find, start with `n` components and subtract one every time an edge joins two different components. Path compression keeps it fast.",
    ],
    91: [
        "The extra edge is the one that connects two nodes that were already connected.",
        "Add the edges one at a time with union-find.",
        "For each edge, find the roots of its endpoints. If they are the same, this edge closes a cycle, so return it. Otherwise union the two groups.",
    ],
    92: [
        "The shortest sequence of one-letter changes is a shortest path in a graph where words are the nodes.",
        "Use breadth-first search starting from `beginWord`. Two words are neighbours if they differ in exactly one letter.",
        "Finding neighbours by comparing all pairs is slow. Instead group the words by patterns like `h*t` and `*ot`: words sharing a pattern are neighbours. Return the BFS depth when you reach `endWord`, or `0` if you never do.",
    ],
}
