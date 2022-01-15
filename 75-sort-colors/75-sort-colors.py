class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count, one_count, two_count = 0,0,0
        for val in nums:
            if val == 0:
                zero_count += 1
            elif val == 1:
                one_count += 1
            elif val == 2:
                two_count += 1
        for i in range(0,zero_count):
            nums[i] = 0
        for i in range(zero_count, zero_count+one_count):
            nums[i] = 1
        for i in range(zero_count+one_count, zero_count+one_count+two_count):
            nums[i] = 2