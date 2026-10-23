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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Running Word Search once per word repeats a lot of work. How could you search for all the words at once?
2. Insert all the words into a trie, then explore the board with DFS, following trie children as you move.
3. Stop exploring a path as soon as the current prefix is not in the trie. Store the full word at its end node so you can collect it, and remove found words (or prune empty branches) to avoid duplicates and speed up later searches.

</details>
