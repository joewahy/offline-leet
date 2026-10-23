# 108. Word Break (Medium)

Given a string `s` and a list of words `wordDict`, return `True` if `s` can be split into a sequence of one or more dictionary words (words may be reused any number of times), otherwise `False`.

## Examples

```
Input:  s = "neetcode", wordDict = ["neet", "code"]
Output: True

Input:  s = "catsincars", wordDict = ["cats", "cat", "sin", "in", "car"]
Output: False
```

## Constraints

- `1 <= len(s) <= 300`
- `1 <= len(wordDict) <= 1000`, `1 <= len(word) <= 20`
- All strings use lowercase letters; the words in `wordDict` are distinct.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Try splitting off the first word. What is left to solve?
2. Let `can[i]` mean the first `i` letters can be split into words. It is true if some earlier `can[j]` is true and `s[j:i]` is a word.
3. Put the words in a set for O(1) lookup. `can[0] = True`. For each `i`, try every `j < i` (you can limit `j` to the longest word length). Return `can[len(s)]`.

</details>
