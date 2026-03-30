class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in numsMap:
            buckets[numsMap[num]].append(num)

        res = []

        for bucket in buckets[::-1]:
            for num in bucket:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res