class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, subSeq):
            if i == len(nums):
                return len(subSeq)
            
            if nums[i] > subSeq[-1]:
                cont = dfs(i+1, subSeq + [nums[i]])
            else:
                cont = 0
            
            skip = dfs(i+1, subSeq)
            new = dfs(i+1, [nums[i]])
            
            return max(cont, skip, new)
        
        return dfs(1, [nums[0]])