class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        beg, end = 1, max(nums) + 1
        index = 0
        while beg <= end:
            mid = (beg + (end - beg)//2)
            
            if sum(ceil(num/mid) for num in nums) <= threshold:
                index = mid
                end = mid - 1
            else:
                beg = mid + 1        
        return index