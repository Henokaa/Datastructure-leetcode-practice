class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        _max = nums[0]
        end = 0
        start = 0
        res = 0
        # [1,3,2,2,2], [1,2,3,3,3]
        for i in range(1, len(nums)):
            if _max > nums[i]:
                end = i
            else:
                _max = nums[i]
   
        _min = nums[-1]
        start = 0
        for i in range(len(nums) - 2, -1, -1):
            if _min < nums[i]:
                start = i
            else:
                _min = nums[i]
        # not like this
        # i, j = 0, 1
        # [1,2,4,5,3] expected 3
        # while j <= len(nums)-1:
        #     if nums[i] >= nums[j]:
        #         start = i
        #         break
        #     j += 1
        #     i += 1

        res = end - start
        return res+1 if res > 0 else 0 

