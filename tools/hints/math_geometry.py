HINTS = {
    136: [
        "A 90 degree rotation can be done as two simpler operations. Which ones?",
        "A clockwise rotation equals a transpose (swap `matrix[i][j]` with `matrix[j][i]`) followed by reversing each row.",
        "Transpose by swapping only the pairs with `j > i`, so you do not swap twice, then call `row.reverse()` on every row. Everything happens in place.",
    ],
    137: [
        "Walk along the outside, then do the same for the inside. What do you need to remember?",
        "Keep four boundaries: top, bottom, left and right. Walk each side, then move the boundaries inwards.",
        "After walking the top row and the right column, only walk the bottom row if `top < bottom`, and the left column if `left < right`, so a single leftover row or column is not visited twice. Stop when the boundaries cross.",
    ],
    138: [
        "If you zero rows and columns as you scan, the new zeros will cause more zeros. How can you avoid that?",
        "First find all the rows and columns that contain a zero, then clear them in a second pass.",
        "Use two sets for the row and column indices. For O(1) extra space, store the markers in the first row and first column, remembering separately whether the first row and the first column themselves contained a zero.",
    ],
    141: [
        "Multiplying `x` by itself `n` times is too slow for large `n`. Can you halve the work at each step?",
        "Use `x^n = (x^(n/2))^2`, with one extra factor of `x` when `n` is odd.",
        "Iterate over the bits of `n`: square `x` at each step, and multiply the result by `x` when the current bit is 1. For negative `n`, use `1 / x` and `-n`.",
    ],
    142: [
        "Do it the way you would on paper, one digit at a time.",
        "The product of digit `i` of `num1` and digit `j` of `num2` contributes to position `i + j + 1` of the result (with a carry into `i + j`).",
        "Use a result array of length `len(num1) + len(num2)`. Loop from the right, add the digit product to `res[i + j + 1]`, then carry `total // 10` into `res[i + j]`. Strip leading zeros at the end, and handle `'0'` specially.",
    ],
    143: [
        "A square is fixed by the query point and the point diagonally opposite it. Which other two corners follow?",
        "Keep a count of each distinct point. For each stored point on a diagonal of the query, check the other two corners.",
        "A stored point `(px, py)` is a valid opposite corner when `abs(px - x) == abs(py - y)` and `px != x`. The other corners are `(px, y)` and `(x, py)`. Add `count(px, py) * count(px, y) * count(x, py)` to the answer.",
    ],
}
