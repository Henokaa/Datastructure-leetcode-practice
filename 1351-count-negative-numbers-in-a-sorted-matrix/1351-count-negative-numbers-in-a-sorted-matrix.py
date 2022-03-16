class Solution:
    def countNegatives(self, grid):
        def bin(row):
            start, end = 0, len(row)-1
            index = -1
            while start <= end:
                mid = start +((end -start) // 2)
                if row[mid]<0:
                    index = mid
                    end = mid - 1
                else:
                    start = mid+1
            if index != -1:
                print (index)
                return len(row) - index
            else:
                return 0

        count = 0
        for row in grid:
            count += bin(row)
        
        return(count)