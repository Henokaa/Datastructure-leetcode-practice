# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leen = 0
        vall = []
        temp = head
        
        while (temp):
            leen = leen + 1
            temp = temp.next
        mid = 0
        if (leen%2 == 0):
            mid = leen/2 -1
        else:
            mid = leen//2
        loop = leen - mid -1
        while(loop != 0):
            head = head.next
            loop = loop -1

        return head