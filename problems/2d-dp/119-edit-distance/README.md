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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Look at the last characters of both words. What if they are equal? If they differ, what are your options?
2. Let `dp[i][j]` be the distance between the first `i` letters of `word1` and the first `j` letters of `word2`.
3. If the letters match, `dp[i][j] = dp[i-1][j-1]`. Otherwise it is 1 plus the minimum of `dp[i-1][j]` (delete), `dp[i][j-1]` (insert) and `dp[i-1][j-1]` (replace). The first row and column are `0, 1, 2, ...`.

</details>
