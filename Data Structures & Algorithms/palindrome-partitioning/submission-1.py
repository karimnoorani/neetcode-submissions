class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []
        
        def isPalindrome(s):
            L, R = 0, len(s)-1
            while L <= R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(substring[:])
                return
            
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    substring.append(s[i:j])
                    dfs(j)
                    substring.pop()
        
        dfs(0)
        return res