class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        res = 0
        for arr in arrays[1:]:
            res = max(abs(arr[0]-maxVal), abs(arr[-1]-minVal))
            maxVal = max(maxVal, arr[-1])
            minVal = min(minVal, arr[0])
        
        return res