# 79. Word Search II (Hard)

Given a grid of characters `board` and a list of distinct strings `words`, return every word from the list that can be spelled by walking through horizontally or vertically adjacent cells. Each cell may be used at most once within a single word. The answer may be in any order.

## Examples

```
Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        words = ["oath", "pea", "eat", "rain"]
Output: ["eat", "oath"]

Input:  board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Constraints

- `1 <= rows, cols <= 12`
- `1 <= len(words) <= 3000`
- `1 <= len(words[i]) <= 10`
- `board` and `words[i]` consist of lowercase letters; all words are distinct.

## Hints

- Searching each word separately repeats a lot of work. Put all the words in a trie and search the board once.
- Prune trie branches that cannot lead to a word any more.
