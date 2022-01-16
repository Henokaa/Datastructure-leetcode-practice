class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x=len(nums)
        c=0
        if(x<3):
            return max(nums)
        nums.sort()
        for i in range(x-1,-1,-1):
            if(nums[i]>nums[i-1] and i!=0):
                c+=1
            if(c==2):
                return nums[i-1]
        return max(nums)
        