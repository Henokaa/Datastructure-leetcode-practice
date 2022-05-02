class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        even = []
        odd = []
        while i < len(nums):
            if nums[i] % 2 == 0:
                even.append(nums[i])
                i += 1
            else:
                odd.append(nums[i])
                i += 1
        return even+odd