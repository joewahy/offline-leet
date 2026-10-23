HINTS = {
    11: [
        "The array is sorted. How does that change the brute force, where you compare every pair?",
        "Put one pointer at each end and look at the sum. If it is too small, which pointer can safely move?",
        "Sum too small: move the left pointer right. Sum too big: move the right pointer left. Each step discards one element for good, giving O(n) time and O(1) space.",
    ],
    12: [
        "Reduce it to a problem you know: if you fix one number, what remains is a two-sum for the negative of it.",
        "Sort the array, fix each number `a` in turn, and use two pointers on the part to its right to find pairs summing to `-a`.",
        "To avoid duplicate triplets, skip a value equal to the previous one for `a`, and after finding a triplet move the left pointer past equal values. Stop early when `a > 0`.",
    ],
    13: [
        "Area is width times the shorter of two heights. Starting with the widest pair, what could you gain by narrowing?",
        "Use two pointers at the ends and compute the area, keeping the best. Then move one pointer inward.",
        "Always move the pointer at the shorter line. Moving the taller one can only shrink the width without raising the limiting height.",
    ],
    14: [
        "Look at one bar. How much water sits on top of it, and which two values decide that?",
        "The water above bar `i` is `min(tallest bar to its left, tallest bar to its right) - height[i]`, never below zero.",
        "Precompute left and right maxima for O(n) with extra space, or use two pointers that move inward from the shorter side while tracking the maximum seen on each side, for O(1) space.",
    ],
}
