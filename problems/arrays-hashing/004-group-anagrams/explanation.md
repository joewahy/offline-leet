### Approach

Anagrams become identical when their letters are sorted, so the sorted string works as a group key. Put each word into a dictionary under its sorted form, then return the groups.

### Complexity

- Time: O(n * k log k) for `n` words of length up to `k`, because sorting each word costs k log k.
- Space: O(n * k) to hold the groups.

### Alternatives

The O(n * k) target replaces the sorted key with a tuple of 26 letter counts. Counting a word is linear in its length, so there is no log factor.
