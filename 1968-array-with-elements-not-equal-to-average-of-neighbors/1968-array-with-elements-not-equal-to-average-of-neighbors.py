class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        A = nums
        A.sort()
        for i in range(1, len(A), 2):
            A[i], A[i - 1] = A[i - 1], A[i]
        return A
        