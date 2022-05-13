class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = format(start, 'b')
        goal = format(goal, 'b')
        start = start.zfill(len(goal))
        goal = goal.zfill(len(start))
        count = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1
        return count
                       
            