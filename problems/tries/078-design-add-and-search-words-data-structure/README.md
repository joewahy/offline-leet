# 78. Design Add and Search Words Data Structure (Medium)

Design a data structure that stores words and can search them with a wildcard.

Implement the class `WordDictionary`:

- `WordDictionary()` creates an empty dictionary.
- `addWord(word)` stores `word`.
- `search(word)` returns `True` if some stored word matches `word`, otherwise `False`. In `word`, the character `.` matches any single letter. All other characters must match exactly, and the lengths must be equal.

## Examples

```
addWord("bad"); addWord("dad"); addWord("mad")
search("pad")   -> False
search("bad")   -> True
search(".ad")   -> True
search("b..")   -> True
```

## Constraints

- `1 <= len(word) <= 20`
- `addWord` words contain lowercase letters; `search` words contain lowercase letters and `.`
- At most `10^5` calls are made, and at most 2 dots appear in any searched word.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Without wildcards this is the normal trie. What changes when `.` appears?
2. Use a trie. When the next character is a letter, follow that child; when it is `.`, you must try every child.
3. Write `search` as a recursive function `go(node, i)`. For `.`, return true if any child's `go(child, i + 1)` is true. At the end of the word, return whether the node is marked as the end of a word.

</details>
