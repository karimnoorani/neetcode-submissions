import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num in count:
            buckets[count[num]].append(num)
        
        i = len(buckets)-1
        while len(res) < k:
            for num in buckets[i]:
                if len(res) == k:
                    break
                res.append(num)
            i -= 1
        
        return res

