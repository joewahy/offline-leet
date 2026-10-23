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
- At most `10000` calls are made, and at most 2 dots appear in any searched word.

## Hints

- Use a trie. When you meet a `.`, try every child at that level.
