class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        L = 0
        res = 1

        for R in range(len(nums)):
            while inc and nums[R] < inc[-1]:
                inc.pop()
            while dec and nums[R] > dec[-1]:
                dec.pop()
            
            inc.append(nums[R])
            dec.append(nums[R])

            while dec[0]-inc[0] > limit:
                if dec[0] == nums[L]:
                    dec.popleft()
                if inc[0] == nums[L]:
                    inc.popleft()
                L += 1
            
            res = max(res, R-L+1)
        
        return res