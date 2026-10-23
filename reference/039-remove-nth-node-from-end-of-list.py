class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        lead = trail = dummy
        for _ in range(n):
            lead = lead.next
        while lead.next:
            lead, trail = lead.next, trail.next
        trail.next = trail.next.next
        return dummy.next
