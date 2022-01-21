class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        stack = []
        mapp = {}
        for i in nums2:
            while stack and i > stack[-1]:
                mapp[stack.pop()] = i
            stack.append(i)
        
        for key in stack:
            mapp[key] = -1
        
        return [mapp[key] for key in nums1]