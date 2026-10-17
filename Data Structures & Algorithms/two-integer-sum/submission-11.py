class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = []

        for index, num in enumerate(nums):
            nums_with_indices.append([num, index])
        
        nums_with_indices.sort()

        left, right = 0, len(nums_with_indices)-1

        while left < right:
            total_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            
            if total_sum == target:
                return sorted([nums_with_indices[left][1], nums_with_indices[right][1]])
            elif total_sum > target:
                right -= 1
            else:
                left += 1
                right = len(nums_with_indices)-1
