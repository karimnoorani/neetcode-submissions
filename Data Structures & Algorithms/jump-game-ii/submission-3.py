class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [[len(nums)-1, 0]]
        for i in range(len(nums)-2, -1, -1):
            while len(steps) > 1 and steps[-1][0]+steps[-1][1] <= i+nums[i]:
                steps.pop()
            
            if i+nums[i] >= steps[-1][0]:
                steps.append([i, steps[-1][0]-i])
        print(steps)    
        return len(steps)-1
            