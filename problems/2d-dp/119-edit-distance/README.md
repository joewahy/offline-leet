# 119. Edit Distance (Medium)

Return the minimum number of single-character operations needed to turn `word1` into `word2`. The allowed operations are:

- insert a character,
- delete a character,
- replace a character with another.

## Examples

```
Input:  word1 = "monkeys", word2 = "money"
Output: 2

Input:  word1 = "horse", word2 = "ros"
Output: 3
```

## Constraints

- `0 <= len(word1), len(word2) <= 500`
- Both words consist of lowercase English letters.

## Hints

- `dp[i][j]` is the distance between the first `i` letters of `word1` and the first `j` of `word2`. If the last letters match it equals `dp[i-1][j-1]`; otherwise 1 plus the best of insert, delete, replace.
