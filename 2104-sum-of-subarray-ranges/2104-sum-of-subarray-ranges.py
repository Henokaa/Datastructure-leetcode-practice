class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        small = 0
        stack = []
        num = nums
        inf = float('inf')
        max_ = 0
        nums = [-inf] + nums + [-inf]
        # [0, 1,   2,    3, 0] num *(left) *(right)
        #nums[-1] ,cur, i  
        for i, val in enumerate(nums):
            while stack and val < nums[stack[-1]]:
                current = stack.pop()
                small += nums[current] * (current - stack[-1]) *(i - current)
            stack.append(i)
    
        stack = []  
        num = [inf] + num + [inf]
        
        for i, val in enumerate(num):
            while stack and val > num[stack[-1]]:
                current = stack.pop()
                max_ += num[current] * (current - stack[-1]) * (i - current)
            stack.append(i)
        return max_ - small