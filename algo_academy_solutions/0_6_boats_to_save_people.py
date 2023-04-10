class Solution:
    def numRescueBoats(self, people, limit):
        ans = 0
        left = 0
        right = len(people) - 1
        people.sort()
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            ans += 1
        
        return ans