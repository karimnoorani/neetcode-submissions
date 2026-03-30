class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(i):
            if i == len(s):
                res.append(path[:])
                return
            
            for j in range(i+1, len(s)+1):
                if self.isPalindrome(s[i:j]):
                    path.append(s[i:j])
                    dfs(j)
                    path.pop()
        
        dfs(0)
        return res


    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True