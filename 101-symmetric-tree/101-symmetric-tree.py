# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        dfs(left)
        if left = None and right = None:
                True
        if not left or not right:
                 false
        if left.val == right.val
                return dfs(left.left, right.right) and dfs(left.right , right.left)
        return false
        '''
        def dfs(left, right):
            if left == None and right == None:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right , right.left)
            return False
        return dfs(root.left, root.right)
            