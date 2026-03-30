class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isValid(t):
            if len(str2) % len(t) != 0 or len(str1) % len(t) != 0:
                return False
            
            if t * (len(str2)//len(t)) != str2 or t * (len(str1)//len(t)) != str1:
                return False
            
            return True
        
        s = str1 if len(str1) < len(str2) else str2

        for i in range(len(s), 0, -1):
            if isValid(s[:i]):
                return s[:i]
        
        return ""