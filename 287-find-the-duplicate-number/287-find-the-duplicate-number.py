class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = left + ((right - left)//2)
            print(mid)
            count = 0
            count = sum(mid >= num for num in nums)
            if count > mid:
                repeat = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return repeat