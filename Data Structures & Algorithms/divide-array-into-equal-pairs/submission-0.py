class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for n in freq:
            if freq[n] % 2 != 0:
                return False
        
        return True