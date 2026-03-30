class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        def backtracking():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    backtracking()
                    count[num] += 1
                    perm.pop()
        
        backtracking()
        return res

