### Approach

Every number gets a plus or minus sign. Keep a dictionary from each reachable running total to the number of ways to reach it. For each number, every total spawns two new totals, one with `+x` and one with `-x`, and the counts carry over. After the last number, `ways[target]` is the answer.

### Complexity

- Time: O(n * sum), the number of distinct totals is at most `2 * sum + 1`.
- Space: O(sum).

### Alternatives

It can be turned into a subset-sum count: choose the numbers with a plus sign so that their sum is `(total + target) / 2`. That needs one array instead of a dictionary.
