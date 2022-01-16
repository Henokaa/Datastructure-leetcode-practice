class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        I = intervals
        I.sort()
        ans = [I[0]]
        for i in I:
            if i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
        return ans