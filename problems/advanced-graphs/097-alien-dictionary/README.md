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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Comparing two neighbouring words reveals at most one ordering rule between letters.
2. Find the first position where two adjacent words differ: the letter in the first word comes before the letter in the second. These rules form a graph.
3. Topologically sort the letters. Return an empty string if there is a cycle, and also if a longer word comes before its own prefix (like `abc` before `ab`). Include letters that appear in no rule.

</details>
