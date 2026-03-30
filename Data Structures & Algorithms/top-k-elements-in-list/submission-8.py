import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        for num in countMap:
            buckets[countMap[num]].append(num)
        
        res = []
        i = len(buckets) - 1
        print(countMap)
        while len(res) < k and i >= 0:
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    break
            i -= 1
        
        return res