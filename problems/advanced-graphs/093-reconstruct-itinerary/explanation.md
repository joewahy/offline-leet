### Approach

Each ticket is used exactly once, so this is an Eulerian path, and the smallest-lexical order is a tie-break. Hierholzer's algorithm finds it. Sort the tickets so that the smallest destination is popped first, then walk: keep going along the next unused ticket until you are stuck. When stuck, that city is the end of the route, so add it to the answer and step back. The answer comes out reversed.

Getting stuck early on a dead end is fine, because that city simply ends up last in the route.

### Complexity

- Time: O(E log E), dominated by sorting the tickets.
- Space: O(E).

### Watch out

The graph is not simply a tree walk, so a greedy "always take the smallest" without the step-back rule can use a ticket that strands the rest.
