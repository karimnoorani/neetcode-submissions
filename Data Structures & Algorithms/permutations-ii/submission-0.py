class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited = set()
        permutation = []

        def backtracking():
            if len(permutation) == len(nums):
                res.add(tuple(permutation))
            
            for i, num in enumerate(nums):
                if i in visited:
                    continue
                permutation.append(num)
                visited.add(i)
                backtracking()
                permutation.pop()
                visited.remove(i)
        
        backtracking()
        return list(res)