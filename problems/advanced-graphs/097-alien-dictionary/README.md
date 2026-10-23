# 97. Alien Dictionary (Hard)

A language uses the lowercase English letters but in an unknown alphabetical order. You are given a list `words` that is sorted according to the rules of that language (compare words letter by letter, and a shorter word that is a prefix of a longer one comes first).

Return a string containing the distinct letters of `words` in a valid order for the language. If several orders are valid, return any of them. If the list cannot be sorted under any order (for example `["abc", "ab"]` or a contradiction), return an empty string `""`.

## Examples

```
Input:  words = ["z", "o"]
Output: "zo"

Input:  words = ["hrn", "hrf", "er", "enn", "rfnn"]
Output: "hernf"     # other valid orders are accepted too

Input:  words = ["abc", "ab"]
Output: ""
```

## Constraints

- `1 <= len(words) <= 300`
- `1 <= len(words[i]) <= 100`
- `words[i]` consists of lowercase English letters.

## Hints

- Compare each pair of neighbouring words: the first position where they differ gives one ordering rule `a before b`.
- Topologically sort the letters using those rules. A cycle means there is no valid order.
