"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        startList = []
        endList = []

        for emp_sched in schedule:
            for interval in emp_sched:
                startList.append(interval.start)
                endList.append(interval.end)
        
        startList.sort(reverse=True)
        endList.sort(reverse=True)
        current_time = startList[-1]
        total_employees = 0
        result = []
        while startList:
            while endList and endList[-1] < startList[-1]:
                current_time = endList.pop()
                total_employees -= 1
            
            if current_time < startList[-1] and total_employees == 0:
                result.append(Interval(current_time, startList[-1]))
            
            current_time = startList.pop()
            total_employees += 1
        
        return result