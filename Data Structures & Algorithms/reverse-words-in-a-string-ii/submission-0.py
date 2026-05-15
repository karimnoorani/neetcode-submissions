class Solution:
    def reverseWords(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        left = 0
        while left < len(s):
            end = left
            while end + 1 < len(s) and s[end + 1] != " ":
                end += 1
            
            right = end
            while left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
            
            left = end + 2
        """
        Do not return anything, modify s in-place instead.
        """
        