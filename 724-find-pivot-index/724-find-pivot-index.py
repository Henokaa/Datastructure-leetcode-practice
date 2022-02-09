class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        
        left = 0
        for i in range(len(nums)):
            right = sums - nums[i] - left
            if left == right:
                return i
            left += nums[i]
        return -1
        