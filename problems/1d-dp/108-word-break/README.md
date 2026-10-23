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

## Hints

- `can[i]` means the first `i` letters can be split. It is true when some `j < i` has `can[j]` and `s[j:i]` is a word.
