from collections import defaultdict
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even_dict = defaultdict(int)
        odd_dict = defaultdict(int)
        n = len(nums)
        ans=0
        for i in range(n):
            if i%2 == 0:
                even_dict[nums[i]] = even_dict.get(nums[i],0) +1
            else:
                odd_dict[nums[i]] = odd_dict.get(nums[i],0) +1
        ke1,ko1,ke2,ko2  = None,None,None,None
        ve1,vo1,ve2,vo2 = 0,0,0,0
        if bool(even_dict):
            ke1,ve1 = max(even_dict.items(), key = lambda k : k[1])
            del even_dict[ke1]
        if bool(odd_dict):
            ko1,vo1 = max(odd_dict.items(), key = lambda k : k[1])
            del odd_dict[ko1]
        if bool(even_dict):
            ke2,ve2 = max(even_dict.items(), key = lambda k : k[1])
        if bool(odd_dict):    
            ko2,vo2 = max(odd_dict.items(), key = lambda k : k[1])
        ans1 = ans2 = ve1+ vo1 
        if(ke1 == ko1) :
            return n - max ( ve1 + vo2, vo1 + ve2)        
        return n - (ve1+ vo1)