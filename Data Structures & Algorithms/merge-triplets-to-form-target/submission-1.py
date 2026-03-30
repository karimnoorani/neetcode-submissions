class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = float('-INF')
        second = float('-INF')
        third = float('-INF')

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            first = max(first, t[0])
            second = max(second, t[1])
            third = max(third, t[2])
        
        return [first, second, third] == target