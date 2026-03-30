class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        
        nums.sort(reverse=True)
        used = [False] * len(nums)
        target = sum(nums)/k

        def dfs(i, k, subSum):
            if k == 0:
                return True
            
            if subSum == target:
                return dfs(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subSum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j+1, k, subSum+nums[j]):
                    return True
                used[j] = False
            return False
        
        return dfs(0, k, 0)