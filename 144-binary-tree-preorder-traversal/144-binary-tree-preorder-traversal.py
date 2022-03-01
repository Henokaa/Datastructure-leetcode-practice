# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []  
        def rec(root):
            if not root:
                return []
            order.append(root.val)
            if root.left:
                rec(root.left)
                
            if root.right:
                rec(root.right)
                
            
            
            return order
        return rec(root)
        