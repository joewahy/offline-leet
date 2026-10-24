### Approach

If the number of cards is not a multiple of the group size, it is impossible. Otherwise take the smallest card value that is still unused. It must start a group, so it needs the next `groupSize - 1` values after it as well. Remove one copy of each. Handling all copies of a value at once (`need = count[x]`) makes the loop do one pass over the sorted distinct values.

### Complexity

- Time: O(n log n), from sorting the distinct values (the group loops add up to O(n) in total).
- Space: O(n) for the counts.
