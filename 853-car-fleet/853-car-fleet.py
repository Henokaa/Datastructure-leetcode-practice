class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrived = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(arrived)[::-1]:
            # append
            stack.append((target - p)/ s)
            # if we get smaller speed we pop
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
            
            