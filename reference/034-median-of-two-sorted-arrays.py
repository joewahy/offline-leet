class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(a) + len(b)
        half = (total + 1) // 2
        lo, hi = 0, len(a)
        inf = float("inf")
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            a_left = a[i - 1] if i > 0 else -inf
            a_right = a[i] if i < len(a) else inf
            b_left = b[j - 1] if j > 0 else -inf
            b_right = b[j] if j < len(b) else inf
            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1
