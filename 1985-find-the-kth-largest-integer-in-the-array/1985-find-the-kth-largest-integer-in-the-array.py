class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n=[]
        for i in nums:
            n.append(int(i))
        return str(sorted(n)[-k])