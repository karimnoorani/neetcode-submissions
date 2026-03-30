import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freqList = [[] for _ in range(len(nums)+1)]

        for num in count:
            freqList[count[num]].append(num)
        
        res = []

        for numList in freqList[::-1]:
            for num in numList:
                if len(res) == k:
                    break
                res.append(num)
            if len(res) == k:
                    break
        
        return res