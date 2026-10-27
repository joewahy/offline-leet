# 77. Implement Trie (Prefix Tree) (Medium)

A trie (prefix tree) stores strings so that you can quickly check whether a word, or a prefix of some word, has been stored.

Implement the class `PrefixTree`:

- `PrefixTree()` creates an empty trie.
- `insert(word)` stores `word`.
- `search(word)` returns `True` if exactly `word` was inserted, otherwise `False`.
- `startsWith(prefix)` returns `True` if some inserted word starts with `prefix`, otherwise `False`.

## Examples

```
insert("Hello")
search("Hello")      -> True
search("Hell")       -> False
startsWith("Hell")   -> True
insert("Hell")
search("Hell")       -> True
```

## Constraints

- `1 <= len(word), len(prefix) <= 1000`
- Strings consist of English letters.
- At most `10^5` calls are made.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Each letter of a word can be a step down a tree. What does a node need to store?
2. Each node holds a dictionary from letter to child node, plus a flag saying whether a word ends there.
3. `insert` walks down, creating missing children, and sets the end flag. `search` walks down and checks the flag. `startsWith` walks down and only checks that the path exists.

</details>
