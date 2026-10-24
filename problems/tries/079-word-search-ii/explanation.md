### Approach

Searching for each word separately repeats work. Instead, put all the words in a trie, then run one depth-first search from every cell, walking the trie in step with the board. If the current letter has no trie child, the branch dies immediately, which is the pruning that makes it fast. When a node marks the end of a word, record it and remove the marker so it is not found twice.

As a further optimization, nodes that no longer lead to any unfound word are deleted on the way back, so later searches skip them.

### Complexity

- Time: O(rows * cols * 3^L), where `L` is the longest word, but heavily pruned in practice.
- Space: O(total characters in the words) for the trie.
