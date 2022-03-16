class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = [0, 0] 
        
        result[0] = self.findStartingIndex(nums, target)   
        result[1] = self.findEndingIndex(nums, target)  
        
        return result 
		
#'''Func one'''
    def findStartingIndex(self, nums, target):
        low = 0
        high = len(nums) - 1
        index = -1
        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid -1
            else: 
                low = mid + 1
        return index
        
# function 2
    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) -1
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if nums[mid] == target:
                index = mid
                low = mid + 1 
            elif nums[mid] > target: 
                high = mid - 1
            else:
                 low = mid + 1  
        return index