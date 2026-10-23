# 104. Palindromic Substrings (Medium)

Return the number of palindromic substrings of `s`. Substrings at different positions count separately, even if they have the same text.

## Examples

```
Input:  s = "abc"
Output: 3          # "a", "b", "c"

Input:  s = "aaa"
Output: 6          # "a" x3, "aa" x2, "aaa"
```

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Testing every substring is too slow. Think about growing palindromes from the middle.
2. Use the same centre expansion as in the longest palindromic substring problem.
3. For each of the `2n - 1` centres, expand while the ends match, and add one to the count for each successful expansion.

</details>
