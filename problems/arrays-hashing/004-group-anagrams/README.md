# 4. Group Anagrams (Medium)

Given a list of strings `strs`, group together the strings that are anagrams of each other. Return the groups in any order; the strings inside a group may also be in any order.

## Examples

```
Input:  strs = ["act", "pots", "tops", "cat", "stop", "hat"]
Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

Input:  strs = [""]
Output: [[""]]
```

## Constraints

- `1 <= len(strs) <= 1000`
- `0 <= len(strs[i]) <= 100`
- `strs[i]` consists of lowercase English letters.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Two words are anagrams exactly when they contain the same letters the same number of times. What single value could describe that for a word?
2. Compute a canonical key for each word (for example its sorted letters, or a count of each letter) and group the words in a dictionary by that key.
3. Sorting each word costs O(k log k); counting letters into a 26-tuple makes the key O(k). Use `defaultdict(list)` and return the dictionary's values.

</details>
