# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = deque([root])
        result = []
        _sum = 0
        a = 0
        while level:
            size = len(level)
            for i in level:
                _sum = _sum + i.val
            result.append(_sum/size)
            _sum = 0
            print("round")
            for i in range(size):
                current = level.popleft()
                
                if current:
                    if current.left:
                        level.append(current.left)
                    if current.right:
                        level.append(current.right)
                else:
                    continue
        return result
                
        