class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        stack = [] 
        stack.append([-1, 0])
        for righti, rightheight in enumerate(height):
            while len(stack) > 1 and stack[-1][1] < rightheight:
                cur_i, cur_height = stack.pop()
                left_i, left_height = stack[-1]
                lowerBound = min(left_height, rightheight)
                numOfBars = righti - left_i - 1
                if lowerBound > 0: 
                    total += (lowerBound - cur_height) * numOfBars     
            stack.append([righti, rightheight])

        return total
        