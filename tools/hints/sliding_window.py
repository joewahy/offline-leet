HINTS = {
    16: [
        "A repeated letter breaks the substring. What do you need to remember to know whether the next letter is a repeat?",
        "Keep a window with a left and a right edge, and a record of the last position of each letter. When the new letter is already inside the window, move the left edge.",
        "Store `last[ch] = index`. If `last[ch] >= left`, set `left = last[ch] + 1`. The answer is the largest `right - left + 1` seen, in O(n) time.",
    ],
    17: [
        "For a window, how many replacements are needed to make all its letters the same?",
        "Replacements needed = window length minus the count of its most frequent letter. The window is valid while that is at most `k`.",
        "Grow the right edge while counting letters. When `length - max_count > k`, move the left edge by one. The answer is the longest valid window, in O(n) time (there are only 26 letters, so finding the max count is cheap).",
    ],
    18: [
        "A permutation of `s1` has exactly the same letter counts as `s1`. What window length are you looking for in `s2`?",
        "Slide a window of length `len(s1)` across `s2` and compare its letter counts with the counts of `s1`.",
        "Update the counts incrementally: add the letter entering on the right, remove the one leaving on the left. Comparing two 26-entry count tables is O(26), so the whole scan is O(n).",
    ],
    19: [
        "A window is valid when it contains every needed letter with enough copies. Once a window is valid, can you make it shorter from the left?",
        "Expand the right edge until the window is valid, then shrink from the left as long as it stays valid, recording the shortest window.",
        "Track how many letters are still missing using a count table. Adding a letter on the right decrements its need. Removing one on the left increments it, and if the need becomes positive the window is invalid again. O(n) overall.",
    ],
    20: [
        "Recomputing `max` for every window works but is slow. Which elements could never be the maximum of any future window?",
        "If a newer element is larger than an older one in the window, the older one can never be the maximum again. Keep candidates in decreasing order.",
        "Use a deque of indices with decreasing values. Before pushing index `i`, pop smaller values from the back; pop the front if it has left the window. The front is the maximum, and the total work is O(n).",
    ],
}
