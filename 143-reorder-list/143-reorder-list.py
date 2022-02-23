# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        sec = slow.next
        slow.next = None
        previous = None
        while sec:
            tmp1 = sec.next
            sec.next = previous
            previous = sec
            sec = tmp1
            
        first, sec = head, previous
        while sec:
            tmp2, tmp3 = first.next, sec.next
            first.next = sec
            sec.next = tmp2
            first, sec = tmp2, tmp3
        