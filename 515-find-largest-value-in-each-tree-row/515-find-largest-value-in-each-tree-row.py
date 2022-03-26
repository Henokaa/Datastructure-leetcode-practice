# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = deque([root])
        max_ = []
        temp = -2**31
        while level:
            for i in level:
                if i.val > temp:
                    temp = i.val
            max_.append(temp)
            temp = -2**31
            size = len(level)
            for i in range(size):
                current = level.popleft()
                if current:
                    if current.left:
                        level.append(current.left)
                    if current.right:
                        level.append(current.right)
                else:
                    continue
        return max_