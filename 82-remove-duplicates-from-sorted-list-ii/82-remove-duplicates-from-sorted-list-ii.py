# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        
        cur = head
        prevNode = dummy
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                distinctNode = cur.next
                while distinctNode and distinctNode.val == cur.val:
                    distinctNode = distinctNode.next
                prevNode.next = distinctNode
                cur = distinctNode
            else:
                prevNode = cur
                cur = cur.next
        
        return dummy.next