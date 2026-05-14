class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        res = 0
        for i in range(len(target)-2, -1, -1):
            res += max(0, target[i]-target[i+1])
        return res