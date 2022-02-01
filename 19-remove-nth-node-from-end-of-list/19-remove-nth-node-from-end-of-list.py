# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        first2 = head
        first = head
        length = 0
        while first2:
            first2 = first2.next
            length +=1
        
        value = length - n - 1
        # if value == -1:
        #     head = None
        print(length)
        while head and head.next and value > 0:
            head = head.next
            value -= 1
        if value == -1:
            head = head.next
            first = head
        else:
            head.next = head.next.next
        
        # length = (length - 1) * 2
        return first
            
            
            