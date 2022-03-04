# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        # when we add the not meaning we pass the right side, lets say the right side and it             # will compute the 
        # right side return max and min of that
        if not root:
            return 0
        # if not root.right and not root.left:
        #     return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) 