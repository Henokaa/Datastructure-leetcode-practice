class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:        
        ans = -1
        left, right = max(weights), sum(weights)
        
        def countDays(capacity):
            i = 0
            myday = 0 
            
            while i < len(weights):
                count = 0
                
                for x in range(i, len(weights)):
                    if count < mid:
                        count += weights[x]
                        i += 1
                    if count == mid:
                        print('stuck in the middle!')
                        break
                    if count > mid:
                        count -= weights[x]
                        i -= 1
                        break
                myday += 1

            # days = curr_weight = 0
            # for i in weights:
            #     if curr_weight + i > capacity:
            #         curr_weight = 0
            #         days += 1
            #     curr_weight += i
            return myday
            # return days+1
        
        while left <= right:
            mid = left + ((right - left)//2)
            d = countDays(mid)
            if d <= days:
                right = mid -1
                ans = mid
            else:
                left = mid + 1
        return ans
 
         