class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s = []
        res = 0
        arr = [0] + arr + [0]
        for i, a in enumerate(arr):
            while s and a < arr[s[-1]]:
                cur_i = s.pop()
                res += arr[cur_i]*(cur_i - s[-1])*(i - cur_i)
            s.append(i)

        return res%(10**9 + 7) 