# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        score = {person: 0 for person in range(n)}

        for person in range(n):
            for nei in range(n):
                if person == nei:
                    continue
                
                if knows(person, nei):
                    score[nei] += 1
                    score[person] -= 1
        
        for person in score:
            if score[person] == n-1:
                return person
        
        return -1