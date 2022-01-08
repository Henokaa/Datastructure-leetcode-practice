class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        bucket = [0]*1440
        for i in range(len(timePoints)):
            t = timePoints[i].split(":")
            hours = int(t[0])
            minute = int(t[1])
            total = hours * 60 + minute
            if (bucket[total]):
                return 0 
            bucket[total] = True
        
        minn = 14000
        first = -1
        prev = -1
        curr = -1
        
        for x in range(len(bucket)):
            if (bucket[x]):
                if (prev == -1):
                    prev = x
                    first = x
                else: 
                    curr = x
                    minn = min(minn, curr - prev)
                    prev = curr
                    
        return min( minn, 1440 - curr + first )