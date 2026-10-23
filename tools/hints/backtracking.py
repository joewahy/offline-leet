HINTS = {
    68: [
        "For each number there are two choices. How many subsets does that give for `n` numbers?",
        "Decide for each element whether to include it, and recurse on the rest. Collect the chosen elements when you reach the end.",
        "Iterative form: start with `[[]]` and, for each number, add a copy of every existing subset with that number appended. The answer has `2^n` subsets.",
    ],
    69: [
        "You may reuse a number, but the same combination in a different order must not appear twice.",
        "Recurse with a start index: at each step choose a number at an index `>= start` and subtract it from the remaining target.",
        "When choosing `nums[i]`, recurse with the same `i` (reuse is allowed) so you never go back to earlier numbers. Stop when the remaining target is `0` (record it) or negative (prune). Sorting lets you stop even earlier.",
    ],
    70: [
        "A permutation fills positions one by one. What choices does each position have?",
        "At each position, pick any number not yet used, then recurse for the next position.",
        "Track the used numbers (a set, a boolean list, or by removing them from a remaining list). When the path has `len(nums)` items, record a copy of it. There are `n!` results.",
    ],
    71: [
        "With duplicates, skipping 'the first 2' and skipping 'the second 2' give the same subset. How do you stop that?",
        "Sort the numbers so equal values are next to each other, then use a start index when recursing.",
        "In the loop over candidates at one recursion level, skip `nums[i]` if `i > start` and `nums[i] == nums[i - 1]`. That keeps each distinct subset exactly once.",
    ],
    72: [
        "Each number can be used once, but the input has duplicates, and duplicate combinations are not allowed.",
        "Sort the candidates. Recurse with a start index, moving to `i + 1` after choosing index `i`.",
        "At the same recursion level, skip a candidate equal to the previous one (`i > start and nums[i] == nums[i - 1]`). Stop the loop when a candidate exceeds the remaining target, since the list is sorted.",
    ],
    73: [
        "You need to try paths through the grid, undoing a step if it leads nowhere. That is backtracking.",
        "Start a depth-first search from every cell that matches the first letter, matching one letter per step in four directions.",
        "Mark the current cell as used (for example overwrite it with `#`) before exploring neighbours, and restore it afterwards. Return true when the position reaches `len(word)`, and false when a cell is out of bounds, used, or a mismatch.",
    ],
    74: [
        "Choose where the first piece ends. Which choices are allowed?",
        "Only prefixes that are palindromes. For each such prefix, recursively partition the rest of the string.",
        "Recurse on a start index: for each `end > start`, if `s[start:end]` is a palindrome, append it, recurse from `end`, then remove it. When `start == len(s)`, record the path. You can precompute a palindrome table to speed up the checks.",
    ],
    75: [
        "Each digit contributes exactly one letter. How many choices does each digit give?",
        "Store the letters for each digit in a map, and build the combinations digit by digit.",
        "Iterative: start with `['']` and, for each digit, replace the list by every existing prefix plus each letter of that digit. Return `[]` for empty input.",
    ],
    76: [
        "Place queens one row at a time. A row can hold only one queen, so the real choice is the column.",
        "A queen at `(r, c)` blocks column `c`, the diagonal `r - c`, and the anti-diagonal `r + c`. Keep a set for each.",
        "Recurse row by row, try each column that is not blocked, mark it, recurse, then unmark it. When all `n` rows are filled, build the board strings from the chosen columns.",
    ],
}
