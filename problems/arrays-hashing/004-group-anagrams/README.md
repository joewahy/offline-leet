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

## Hints

- Anagrams share a common "signature". What could it be?
- Use that signature as a dictionary key.
