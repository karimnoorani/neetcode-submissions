class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats.sort()
        students.sort()

        for seat, student in zip(seats, students):
            res += abs(seat-student)
        
        return res