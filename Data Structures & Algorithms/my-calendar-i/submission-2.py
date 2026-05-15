from sortedcontainers import SortedList

class MyCalendar:
    
    def __init__(self):
        self.times = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        L, R = 0, len(self.times)-1
        print([startTime, endTime], self.times)
        while L <= R:
            M = (L + R) // 2

            if startTime >= self.times[M][1]:
                L = M + 1
            elif endTime <= self.times[M][0]:
                R = M - 1
            else:
                return False
        
        self.times.add([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)