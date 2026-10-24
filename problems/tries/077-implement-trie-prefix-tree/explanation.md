### Approach

A trie stores words as paths of letters. Each node maps a letter to its child node, and a `$` marker on a node says that a word ends there. `insert` walks and creates nodes. `search` follows the path and also checks for the marker. `startsWith` only needs the path to exist.

### Complexity

- Time: O(L) per operation, where `L` is the length of the word or prefix.
- Space: O(total characters inserted).

### Watch out

`search("app")` must be false when only `"apple"` was inserted. That is what the end marker is for.
