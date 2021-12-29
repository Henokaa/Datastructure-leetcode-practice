class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        sortednums = sorted(nums)
        for i in range(len(sortednums)):
            if sortednums[i] == target:
                ans.append(i)
                
        return ans