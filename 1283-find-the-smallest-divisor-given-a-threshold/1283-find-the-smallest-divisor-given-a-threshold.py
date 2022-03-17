class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        beg, end = 1, max(nums)
        index = -1
        while beg <= end:
            mid = beg + ((end - beg)//2)
            x = sum(ceil(i/mid) for i in nums)
            if x <= threshold:
                index = mid
                end = mid -1
            else:
                beg = mid + 1
        return index
                
            