class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:        
        ans = -1
        left, right = max(weights), sum(weights)
        
        def countDays(capacity):
            days = curr_weight = 0
            for i in weights:
                if curr_weight + i > capacity:
                    curr_weight = 0
                    days += 1
                curr_weight += i
                
            return days+1
        
        while left <= right:
            mid = left + ((right - left)//2)
            d = countDays(mid)
            # print(d,mid)
            if d <= days:
                right = mid -1
                ans = mid
            else:
                left = mid + 1
        return ans
 
         