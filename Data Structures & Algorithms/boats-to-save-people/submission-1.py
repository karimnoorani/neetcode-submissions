class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        totalBoats = 0

        while l <= r:
            if people[l] <= limit-people[r]:
                l += 1
            
            r -= 1
            totalBoats += 1
        
        return totalBoats
