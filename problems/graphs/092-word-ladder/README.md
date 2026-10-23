# 92. Word Ladder (Hard)

You are given a `beginWord`, an `endWord` and a list `wordList`. A transformation changes exactly one letter at a time, and every word you pass through (except `beginWord`) must be in `wordList`.

Return the number of words in the shortest sequence from `beginWord` to `endWord`, counting both ends. If no sequence exists, return `0`. `beginWord` does not need to be in `wordList`.

## Examples

```
Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5          # hit -> hot -> dot -> dog -> cog

Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0          # "cog" is not in the list
```

## Constraints

- `1 <= len(beginWord) <= 10`, and `len(endWord) == len(beginWord)`
- `1 <= len(wordList) <= 3000`, and every word has the same length
- Words consist of lowercase letters; the words in `wordList` are unique.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The shortest sequence of one-letter changes is a shortest path in a graph where words are the nodes.
2. Use breadth-first search starting from `beginWord`. Two words are neighbours if they differ in exactly one letter.
3. Finding neighbours by comparing all pairs is slow. Instead group the words by patterns like `h*t` and `*ot`: words sharing a pattern are neighbours. Return the BFS depth when you reach `endWord`, or `0` if you never do.

</details>
