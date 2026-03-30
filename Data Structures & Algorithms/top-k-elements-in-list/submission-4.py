class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        
        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1
        
        count = [[] for i in range(len(nums) + 1)]
        print(count)
        for num in numsMap:
            count[numsMap[num]].append(num)

        res = []
        i = len(nums)
        while i > -1 and len(res) < k:
            for item in count[i]:
                if len(res) == k:
                    break
                res.append(item)
            i -=1
        return res