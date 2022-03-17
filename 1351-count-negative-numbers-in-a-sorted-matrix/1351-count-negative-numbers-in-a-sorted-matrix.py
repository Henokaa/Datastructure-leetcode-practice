class Solution:
    def countNegatives(self, grid):
        cur = 0
        for i in grid:
            index = -1
            left, right = 0 , len(i)- 1
            while left <= right:
                mid = left + ((right - left) // 2)
                if i[mid] < 0:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if index != -1:
                cur += len(i) - index
                
        return cur
                