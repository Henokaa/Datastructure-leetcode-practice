# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left =  dummy
        right = dummy
        
        while n > 0 and right.next:
            right = right.next
            print(right)
            n -= 1
        
        while right.next:
            left = left.next
            right = right.next
        
        
        left.next = left.next.next
        return dummy.next
            
            
            