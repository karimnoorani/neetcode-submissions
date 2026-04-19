class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        buckets = [0 for _ in range(101)]
        
        for h in heights:
            buckets[h] += 1
        
        sorted_list = []
        for i in range(101):
            for j in range(buckets[i]):
                sorted_list.append(i)
        
        res = 0
        for i, h in enumerate(heights):
            if sorted_list[i] != h:
                res += 1
        
        return res
        