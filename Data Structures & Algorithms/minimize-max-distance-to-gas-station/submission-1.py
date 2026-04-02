class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def isFeasible(p):
            count = 0
            for i in range(len(stations)-1):
                count += int((stations[i+1]-stations[i])/p)
            return count <= k
        
        low = 0
        high = stations[-1] - stations[0]
        
        while high - low > 1e-6:
            M = (low+high) / 2.0
            if isFeasible(M):
                high = M
            else:
                low = M
        
        return low