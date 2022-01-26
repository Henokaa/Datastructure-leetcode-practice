class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        if n == 1:
            return True
        res = self.isPowerOfThree(n / 3)
        return res
        