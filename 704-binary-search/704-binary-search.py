class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            if nums[int(mid)] < target:
                left = mid + 1
            elif nums[int(mid)] > target:
                right = mid - 1
            else:
                return int(mid)
            
        return -1
        