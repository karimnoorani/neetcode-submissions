class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        currentSeq = 1
        maxSeq = 1
        pattern = 0

        for i in range(1, len(arr)):
            if pattern == 0 and arr[i] != arr[i-1]:
                pattern = (arr[i]-arr[i-1])/abs(arr[i]-arr[i-1])
                currentSeq += 1
                maxSeq = max(maxSeq, currentSeq)
            elif pattern == 1 and arr[i] < arr[i-1]:
                currentSeq += 1
                maxSeq = max(maxSeq, currentSeq)
                pattern = -1
            elif pattern == -1 and arr[i] > arr[i-1]:
                currentSeq += 1
                maxSeq = max(maxSeq, currentSeq)
                pattern = 1
            elif arr[i] == arr[i-1]:
                pattern = 0
                currentSeq = 1
            else:
                currentSeq = 2
                pattern = (arr[i]-arr[i-1])/abs(arr[i]-arr[i-1])
                maxSeq = max(maxSeq, currentSeq)
        
        return maxSeq

            