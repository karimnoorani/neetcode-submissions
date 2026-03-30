class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        currentSeq = 1
        maxSeq = 1
        pattern = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]: newPattern = 1
            elif arr[i] < arr[i-1]: newPattern = -1
            else: newPattern = 0

            if pattern != 0 and pattern == (newPattern*-1):
                currentSeq += 1
            elif newPattern == 0:
                currentSeq = 1
            else:
                currentSeq = 2
            
            pattern = newPattern
            maxSeq = max(maxSeq, currentSeq)
        
        return maxSeq