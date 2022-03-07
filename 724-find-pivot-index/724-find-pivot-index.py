class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0]
        right = [0]
        for i in nums:
            left.append(left[-1] + i)
        left.pop()
        
        for a in range(len(nums)-1,0,-1):
            right.append(right[-1] + nums[a])
        i = 0
        x = len(right) - 1
        while i < len(nums):
            if (left[i] == right[x]):
                return i   
            x -=1
            i += 1
        return -1

        
            
        