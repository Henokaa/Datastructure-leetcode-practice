class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = heapq.nlargest(k, nums) # run time O(n+klgn)
        return ans[-1]
'''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums) # run time O(k)
        for _ in range(k):
            ans = heapq.heappop(nums) # run time O(nlgk)
        return -ans    
'''