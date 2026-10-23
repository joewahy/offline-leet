HINTS = {
    4: [
        "Two words are anagrams exactly when they contain the same letters the same number of times. What single value could describe that for a word?",
        "Compute a canonical key for each word (for example its sorted letters, or a count of each letter) and group the words in a dictionary by that key.",
        "Sorting each word costs O(k log k); counting letters into a 26-tuple makes the key O(k). Use `defaultdict(list)` and return the dictionary's values.",
    ],
    5: [
        "You need two things: how often each number appears, and which `k` counts are the largest.",
        "Count with a dictionary, then either sort by count, keep a min-heap of size `k`, or use buckets indexed by frequency.",
        "Bucket sort gives O(n): a frequency is at most `len(nums)`, so make a list of that size where index `f` holds the numbers that appear `f` times, then read it from the end.",
    ],
    6: [
        "A separator like `,` fails as soon as a string contains it. What information could you store instead of relying on a separator?",
        "Write each string's length, then a marker, then the string itself. When decoding, the length tells you exactly how many characters to take.",
        "Read digits up to the marker `#` to get the length `n`, take the next `n` characters (even if they include `#` or digits), then continue after them. An empty string is just `0#`.",
    ],
    7: [
        "Division is not allowed, and zeros would break it anyway. Think about what is to the left of each position and what is to the right.",
        "The answer for index `i` is (product of everything left of `i`) times (product of everything right of `i`). Build the left products in one pass.",
        "Fill the output with prefix products going right, then walk from the end with a running suffix product and multiply it into the output. That uses O(n) time and O(1) extra space.",
    ],
    8: [
        "You never need to solve the puzzle, only to detect a repeated digit in a row, a column, or a 3x3 box.",
        "Keep a set of seen digits for each row, each column, and each box, and check them as you scan each filled cell once.",
        "The box for cell `(r, c)` is `(r // 3, c // 3)`. One set of tuples like `('r', r, digit)`, `('c', c, digit)`, `('b', r // 3, c // 3, digit)` covers all three rules.",
    ],
    9: [
        "Sorting works but costs O(n log n). Which numbers can possibly be the start of a run?",
        "Put all numbers in a set. A number `x` starts a run only if `x - 1` is not in the set.",
        "From each start, count upward while `x + 1` is in the set. Each number belongs to exactly one run, so the total work is O(n).",
    ],
}
