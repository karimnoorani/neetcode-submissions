class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right, deletion_used):
            while left < right:
                if s[left] != s[right]:
                    if deletion_used:
                        return False
                    return isPalindrome(left+1, right, True) or isPalindrome(left, right-1, True)
                
                left += 1
                right -= 1
            
            return True
        
        return isPalindrome(0, len(s)-1, False)