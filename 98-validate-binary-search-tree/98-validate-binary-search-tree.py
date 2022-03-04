# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # function for finding the inorder traversal result
        def inOrder(root):
            ans = []
            if root:
                ans += inOrder(root.left) + [root.val] + inOrder(root.right)
            return ans
        
        output = inOrder(root)  # store the inorder traversal in output array
        
        # check whether output array is sorted or not
        # if sorted then, Valid BST
        # otherwise, not a BST
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:  # i.e output array is not sorted
                return False

        return True
            
    