# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        mapp = []
        i = 0
        while head:
            x = i
            while stack and head.val > stack[-1][0]:
                mapp.append([stack[-1][1], head.val])
                stack.pop()
            stack.append([head.val, i])
            head = head.next
            i += 1
        result = [0]*i
        print(mapp)
        while mapp:
            result[mapp[-1][0]] = mapp[-1][1]
            mapp.pop()
        return result
        # while stack:
        #     mapp.insert(stack[-1][1], 0)
        #     stack.pop()
        # return mapp
            
        