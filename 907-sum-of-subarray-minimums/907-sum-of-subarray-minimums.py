class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s = []
        res = 0
        arr = [0] + arr + [0]
        # lets take 1 for eg. how many times 1 come be minimum in the left side 2, counting itself. how many times 1 in             # the right side 3. 3 * 2 = 6. can't be addition. because the element before it 3 will affect it {3,1}, [3,1,2]
        # [3, 1, 2, 4]
        #
        for i, val in enumerate(arr):
            while s and val < arr[s[-1]]:
                cur_i = s.pop()
                res += arr[cur_i]*(cur_i - s[-1])*(i - cur_i)
            s.append(i)

        return res%(10**9 + 7) 