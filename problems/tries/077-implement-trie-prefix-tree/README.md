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
- At most `10000` calls are made.

## Hints

- Each node holds a dictionary of children and a flag that says whether a word ends there.
