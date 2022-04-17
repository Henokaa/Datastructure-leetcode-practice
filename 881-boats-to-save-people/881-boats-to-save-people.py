class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        answer = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                answer += 1
                right -= 1
                left += 1
            elif people[right] <= limit:
                answer += 1
                right -= 1
            
        return answer
 
        