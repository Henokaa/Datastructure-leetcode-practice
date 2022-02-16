# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(0,head)
        previous, cur = new, head
        
        while cur and cur.next:
            nextt = cur.next.next
            last = cur.next
            
            last.next = cur
            cur.next = nextt
            previous.next = last
            
            previous = cur
            cur = nextt
            
        return new.next