HINTS = {
    101: [
        "At each house you either rob it or skip it. What does robbing it rule out?",
        "Let `best(i)` be the most you can get from the first `i` houses. It is the larger of skipping house `i` or robbing it.",
        "`best(i) = max(best(i-1), best(i-2) + nums[i])`. You only need the last two values, so two variables give O(1) space.",
    ],
    102: [
        "The first and last houses are neighbours. What does that stop you from doing?",
        "You cannot rob both of them. So the answer is the better of two plain House Robber problems.",
        "Solve House Robber on `nums[1:]` (skip the first house) and on `nums[:-1]` (skip the last house), and return the larger result. Handle a single house separately.",
    ],
    103: [
        "Every palindrome has a centre. How many possible centres does a string of length `n` have?",
        "Expand outwards from each centre while the two ends match, and remember the longest result.",
        "There are `2n - 1` centres: each character, and each gap between two characters (for even lengths). Expansion costs O(n) per centre, so O(n^2) overall.",
    ],
    104: [
        "Testing every substring is too slow. Think about growing palindromes from the middle.",
        "Use the same centre expansion as in the longest palindromic substring problem.",
        "For each of the `2n - 1` centres, expand while the ends match, and add one to the count for each successful expansion.",
    ],
    105: [
        "At each position you may read one digit or two. Which choices are valid?",
        "One digit is valid if it is not `0`. Two digits are valid if they form a number from 10 to 26.",
        "Let `ways(i)` be the count for the suffix starting at `i`, with `ways(n) = 1`. If `s[i] != '0'`, then `ways(i) = ways(i+1)`, plus `ways(i+2)` when `s[i:i+2] <= '26'`. Otherwise `ways(i) = 0`.",
    ],
    106: [
        "Taking the biggest coin each time can give the wrong answer. Think about the fewest coins for every smaller amount.",
        "Let `dp[a]` be the fewest coins for amount `a`. To make `a`, the last coin is some `c`, so look at `dp[a - c]`.",
        "`dp[0] = 0` and `dp[a] = 1 + min(dp[a - c])` over coins `c <= a` (use infinity when impossible). Fill from 1 up to `amount`, and return `-1` if `dp[amount]` is still infinity.",
    ],
    107: [
        "Two negative numbers multiply to a positive. What does that do to the smallest product so far?",
        "Track both the largest and the smallest product of a subarray ending at the current position.",
        "At each number `x`, the new max is `max(x, hi * x, lo * x)` and the new min is `min(x, hi * x, lo * x)`, computed from the old values. The answer is the best max seen. A zero resets the run automatically.",
    ],
    108: [
        "Try splitting off the first word. What is left to solve?",
        "Let `can[i]` mean the first `i` letters can be split into words. It is true if some earlier `can[j]` is true and `s[j:i]` is a word.",
        "Put the words in a set for O(1) lookup. `can[0] = True`. For each `i`, try every `j < i` (you can limit `j` to the longest word length). Return `can[len(s)]`.",
    ],
    109: [
        "For each element, what is the longest increasing subsequence that ends there?",
        "It is 1 plus the best among the earlier, smaller elements. This gives an O(n^2) solution.",
        "For O(n log n), keep a list `tails` where `tails[k]` is the smallest possible last value of an increasing subsequence of length `k + 1`. For each number, binary search (`bisect_left`) its place: replace that entry, or append if it is larger than all of them. The answer is `len(tails)`.",
    ],
    110: [
        "If the total is odd, can the two halves be equal? If it is even, what exactly are you looking for?",
        "You need a subset that sums to `total / 2`. That is a subset-sum problem.",
        "Keep the set of reachable sums (or a boolean array up to `total / 2`). For each number, add it to every reachable sum. If `total / 2` becomes reachable, return true. A bitmask `reach |= reach << x` does it compactly.",
    ],
}
