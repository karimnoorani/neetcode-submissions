class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        s1P = 0 
        s2P = 0

        while s1P < len(slots1) and s2P < len(slots2):
            start1, end1 = slots1[s1P][0], slots1[s1P][1]
            start2, end2 = slots2[s2P][0], slots2[s2P][1]
            
            if min(end1, end2) - max(start1, start2) >= duration:
                return [max(start1, start2), max(start1, start2)+duration]
            
            if end1 < end2:
                s1P += 1
            else:
                s2P += 1
        
        return []