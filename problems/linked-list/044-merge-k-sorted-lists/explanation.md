### Approach

The smallest unmerged node is always at the front of one of the `k` lists. Keep those `k` front nodes in a min-heap. Repeatedly pop the smallest, attach it to the result, and push its successor if it has one.

The heap stores `(value, list index, node)`. The index breaks ties so Python never has to compare two nodes.

### Complexity

- Time: O(N log k), where `N` is the total number of nodes. Each node enters and leaves a heap of size at most `k`.
- Space: O(k) for the heap.

### Alternatives

Merging the lists two at a time works too. Merge them in pairs, like a tournament, to also get O(N log k). Merging them one after another into a growing result is O(N * k).
