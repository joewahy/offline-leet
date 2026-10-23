HINTS = {
    111: [
        "To reach a cell you must come from the cell above it or the cell to its left.",
        "So the number of ways to a cell is the sum of the ways to those two cells. The first row and first column each have one way.",
        "Keep one row of the table and update it row by row: `row[j] += row[j - 1]`. It is also the binomial coefficient `C(m + n - 2, m - 1)`.",
    ],
    112: [
        "Compare the last characters of the two strings. What happens if they match? If they do not?",
        "Let `dp[i][j]` be the LCS of the first `i` characters of `text1` and the first `j` characters of `text2`.",
        "If the characters match, `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`. You only need the previous row.",
    ],
    113: [
        "Each day you are in one of a few states: holding a share, just sold, or resting. What can you do from each?",
        "Track the best profit for each state at the end of each day: `hold`, `sold`, and `rest`.",
        "`hold = max(hold, rest - price)`, `sold = old_hold + price`, `rest = max(rest, old_sold)`. Use the old values on the right side of each update. The answer is `max(sold, rest)` after the last day.",
    ],
    114: [
        "Counting combinations differs from counting sequences: `1 + 2` and `2 + 1` are the same combination.",
        "Process one coin type at a time, so each combination is counted once, in a fixed order of coins.",
        "Let `ways[a]` be the number of combinations for amount `a`, with `ways[0] = 1`. For each coin `c`, loop `a` from `c` up to `amount` and do `ways[a] += ways[a - c]`. The loop over coins must be the outer one.",
    ],
    115: [
        "Each number gets a plus or a minus. How many different running totals can exist?",
        "Track how many ways each running total can be reached, one number at a time.",
        "Keep a dictionary `ways[total] = count`. For each number `x`, build a new dictionary where each `total` contributes to `total + x` and to `total - x`. The answer is `ways[target]`. (Alternative: count the subsets that sum to `(total + target) / 2`.)",
    ],
    116: [
        "If the lengths of `s1` and `s2` do not add up to `len(s3)`, you can stop right away. Otherwise, each next character of `s3` has to come from one of the two strings.",
        "Let `dp[i][j]` be whether the first `i` letters of `s1` and the first `j` letters of `s2` can form the first `i + j` letters of `s3`.",
        "`dp[i][j]` is true if `dp[i-1][j]` is true and `s1[i-1] == s3[i+j-1]`, or `dp[i][j-1]` is true and `s2[j-1] == s3[i+j-1]`. `dp[0][0]` is true. One row is enough.",
    ],
    117: [
        "From a cell, the longest path never depends on how you arrived there, because you only move to larger values.",
        "Use DFS from every cell, and remember the answer for each cell so you compute it only once (memoization).",
        "`longest(r, c) = 1 + max(longest(neighbour))` over neighbours with a larger value, or `1` if there are none. Strictly increasing paths cannot loop, so caching is safe. The total time is O(rows * cols).",
    ],
    118: [
        "Compare the current letter of `s` with the current letter of `t`. When they are equal, you have two choices.",
        "Let `dp[j]` be the number of ways to form the first `j` letters of `t` from the letters of `s` seen so far.",
        "For each letter `c` of `s`, going `j` from `len(t)` down to `1`: if `t[j-1] == c`, add `dp[j-1]` to `dp[j]`. Start with `dp[0] = 1`. Going downwards makes sure each letter of `s` is used at most once per step.",
    ],
    119: [
        "Look at the last characters of both words. What if they are equal? If they differ, what are your options?",
        "Let `dp[i][j]` be the distance between the first `i` letters of `word1` and the first `j` letters of `word2`.",
        "If the letters match, `dp[i][j] = dp[i-1][j-1]`. Otherwise it is 1 plus the minimum of `dp[i-1][j]` (delete), `dp[i][j-1]` (insert) and `dp[i-1][j-1]` (replace). The first row and column are `0, 1, 2, ...`.",
    ],
    120: [
        "Choosing the first balloon to burst is hard, because the neighbours change. Try thinking about the last balloon to burst instead.",
        "If balloon `k` is the last one burst in a range, its neighbours are the fixed borders of the range, and the two sides become independent subproblems.",
        "Pad `nums` with `1` on both ends. `dp[l][r]` is the best for the balloons strictly between `l` and `r`: the maximum over `k` of `dp[l][k] + dp[k][r] + a[l] * a[k] * a[r]`. Fill it by increasing range length. This is O(n^3).",
    ],
    121: [
        "Compare characters from the front or the back. What special cases does `*` create?",
        "Let `dp[i][j]` be whether the first `i` letters of `s` match the first `j` characters of `p`. Handle a normal character or `.` first.",
        "For a plain character or `.`, `dp[i][j] = dp[i-1][j-1]` if they match. For `x*`, either use it zero times (`dp[i][j-2]`) or, if `x` matches `s[i-1]`, use one more copy (`dp[i-1][j]`). Patterns like `a*b*` can match the empty string, so initialise the first row.",
    ],
}
