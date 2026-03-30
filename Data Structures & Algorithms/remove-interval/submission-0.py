class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
                res.append(interval)
            else:
                pre = [min(interval[0], toBeRemoved[0]), toBeRemoved[0]]
                post = [toBeRemoved[1], max(toBeRemoved[1], interval[1])]

                if pre[1] - pre[0] > 0:
                    res.append(pre)
                
                if post[1] - post[0] > 0:
                    res.append(post)
        
        return res