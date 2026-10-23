class Solution:
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second, slow.next = slow.next, None
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
        first, second = head, prev
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
