# 127. Merge Triplets to Form Target Triplet (Medium)

`triplets[i] = [a, b, c]` are triples of integers, and `target = [x, y, z]` is the triple you want to build.

You may repeatedly pick two different triplets `i` and `j` and replace `triplets[j]` with `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

Return `True` if, after any number of such operations, `target` appears as one of the triplets, otherwise `False`.

## Examples

```
Input:  triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: True

Input:  triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: False
```

## Constraints

- `1 <= len(triplets) <= 10000`
- `1 <= a, b, c, x, y, z <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Merging takes the maximum at each position, so it can only increase values. Which triplets can never be used?
2. Any triplet with a value larger than the target in some position can never be used, because the maximum would overshoot.
3. Among the usable triplets, take the position-wise maximum. If it equals the target, return true. Equivalently, check that each target position is matched by some usable triplet.

</details>
