# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        order = []  
        def rec(root):
            if not root:
                return []
            return rec(root.left) + rec(root.right) + [root.val]
        return rec(root)
