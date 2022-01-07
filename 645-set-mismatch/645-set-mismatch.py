class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep, mis = None, None
        N = len(nums)
        lookup = Counter(nums)
        
        for i in range(1, N+1):
            if i not in lookup: mis = i
            if lookup[i]>1: rep = i
        
        return [rep, mis]